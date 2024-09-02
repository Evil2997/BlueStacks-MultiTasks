from typing import Dict
from typing import Optional, Tuple

import cv2
import mss
import numpy as np
import pytesseract
from PIL import Image

from modules.screens import find_template_in_region


def capture_full_screen_or_region(region: Optional[Tuple[int, int, int, int]] = (0, 0, 1920, 1080)) -> Image.Image:
    """
    Захватывает скриншот всего экрана или указанной области экрана.

    :param region: Область для захвата (левая верхняя x, левая верхняя y, правая нижняя x, правая нижняя y).
    Если None, захватывается весь экран.
    :return: Изображение в формате PIL.
    """
    with mss.mss() as screen_capturer:
        screenshot = screen_capturer.grab(region) if region else screen_capturer.grab(screen_capturer.monitors[1])
        img = Image.frombytes('RGB', screenshot.size, screenshot.rgb)
        return img


def extract_text_and_coordinates(image: Image.Image, lang: str = 'rus') -> Dict[str, Dict[int, Tuple[int, int]]]:
    """
    Извлекает текст и его координаты из изображения с помощью Tesseract OCR.

    :param image: Изображение, из которого нужно извлечь текст.
    :param lang: Язык для OCR (по умолчанию 'rus').
    :return: Словарь с данными, где ключ - текст, а значение - словарь индексов и координат.
    """
    custom_config = r'--oem 3 --psm 11'
    ocr_data = pytesseract.image_to_data(image, lang=lang, config=custom_config, output_type=pytesseract.Output.DICT)

    coordinates = {}
    for i in range(len(ocr_data['text'])):
        text = ocr_data['text'][i].strip()
        if text:
            x, y, w, h = ocr_data['left'][i], ocr_data['top'][i], ocr_data['width'][i], ocr_data['height'][i]
            x_center, y_center = x + w // 2, y + h // 2
            if text not in coordinates:
                coordinates[text] = {}
            coordinates[text][i] = (x_center, y_center)
    return coordinates


def visual_scan_tracker(region: Optional[Tuple[int, int, int, int]] = (0, 0, 1920, 1080),
                        lang: str = 'rus',
                        target_phrase: str = '',
                        occurrence_index: int = 0) -> Optional[Tuple[int, int]] | None:
    """
    Сканирует экран, находит указанную фразу и возвращает координаты указанного появления этой фразы.

    :param region: Область для захвата (если None, захватывается весь экран).
    :param lang: Язык для OCR (по умолчанию 'rus').
    :param target_phrase: Фраза, которую нужно найти.
    :param occurrence_index: Индекс вхождения (0 для первого, 1 для второго и т.д.).
    :return: Координаты (x, y) указанного появления фразы или None, если фраза не найдена.
    """
    img = capture_full_screen_or_region(region)
    coordinates = extract_text_and_coordinates(img, lang)

    if target_phrase in coordinates:
        x, y = list(coordinates[target_phrase].values())[occurrence_index]
        return x, y
    return None


def is_text_yellow(image: Image.Image, coin_center: Tuple[int, int]) -> bool:
    """
    Проверяет, является ли текст рядом с центром найденной монетки желтым.

    :param image: Скриншот экрана в формате PIL.
    :param coin_center: Координаты центра монетки в формате (x_center, y_center).
    :return: True, если текст желтый, иначе False.
    """
    x_center, y_center = coin_center
    text_region = image.crop((x_center, y_center - 20, x_center + 150,
                              y_center + 20))  # Предполагаем, что текст находится справа от центра монетки

    # Преобразуем текстовую область в HSV для определения цвета
    text_region_np = np.array(text_region)
    hsv_image = cv2.cvtColor(text_region_np, cv2.COLOR_RGB2HSV)

    # Диапазон для желтого цвета
    lower_yellow = np.array([20, 150, 150])
    upper_yellow = np.array([35, 255, 255])

    mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    yellow_ratio = np.sum(mask > 0) / (mask.shape[0] * mask.shape[1])

    return yellow_ratio > 0.5  # Если больше 50% области желтого цвета, считаем, что текст желтый


def extract_text_near_coin(image: Image.Image, coin_center: Tuple[int, int], lang: str = 'rus') -> str:
    """
    Извлекает текст рядом с центром найденной монетки.

    :param image: Скриншот экрана в формате PIL.
    :param coin_center: Координаты центра монетки в формате (x_center, y_center).
    :param lang: Язык для OCR (по умолчанию 'rus').
    :return: Извлеченный текст.
    """
    x_center, y_center = coin_center
    text_region = image.crop((x_center + 10, y_center - 20, x_center + 150,
                              y_center + 20))  # Предполагаем, что текст находится справа от центра монетки
    custom_config = r'--oem 3 --psm 6'
    extracted_text = pytesseract.image_to_string(text_region, lang=lang, config=custom_config)
    return extracted_text.strip()


def find_coin_and_check_text(
        template_name: str, region: Optional[Tuple[int, int, int, int]] = (0, 0, 1920, 1080)
) -> Optional[Tuple[int, int]] | None:

    """
    Ищет монетку на экране и проверяет, является ли текст рядом с ней желтым.

    :param region:
    :param template_name: Имя изображения-шаблона монетки.
    :return: True, если текст рядом с монеткой желтый; иначе False.
    """
    coin_center = find_template_in_region(template_name)

    with mss.mss() as screen_capturer:
        screenshot = screen_capturer.grab(region) if region else screen_capturer.grab(screen_capturer.monitors[1])
        image = Image.frombytes('RGB', screenshot.size, screenshot.rgb)

    if coin_center:
        if is_text_yellow(image, coin_center):
            return coin_center

    return None
