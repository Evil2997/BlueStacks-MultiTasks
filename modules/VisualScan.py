from typing import Dict, List
from typing import Optional, Tuple

import cv2
import mss
import numpy as np
import pytesseract
from PIL import Image, ImageGrab

from modules import config___oem_3__psm_11, config___oem_3__psm_6
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
    ocr_data = pytesseract.image_to_data(image, lang=lang, config=config___oem_3__psm_11, output_type=pytesseract.Output.DICT)

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


def is_text_yellow(image: Image.Image, coin_center: Tuple[int, int],
                   lower_yellow: Optional[np.ndarray] = None,
                   upper_yellow: Optional[np.ndarray] = None) -> bool:
    """
    Проверяет, является ли текст рядом с центром найденной монетки заданного желтого цвета.

    :param image: Скриншот экрана в формате PIL.
    :param coin_center: Координаты центра монетки в формате (x_center, y_center).
    :param lower_yellow: Нижняя граница диапазона желтого цвета в HSV (обязательный параметр).
    :param upper_yellow: Верхняя граница диапазона желтого цвета в HSV (обязательный параметр).
    :return: True, если текст заданного желтого цвета; иначе False.
    :raises ValueError: Если диапазон желтого цвета не передан.
    """
    if lower_yellow is None or upper_yellow is None:
        raise ValueError("Диапазон желтого цвета (lower_yellow и upper_yellow) должен быть передан!")

    x_center, y_center = coin_center
    text_region = image.crop((x_center, y_center - 20, x_center + 150, y_center + 20))  # Текст справа от монетки

    # Преобразуем текстовую область в HSV для определения цвета
    text_region_np = np.array(text_region)
    hsv_image = cv2.cvtColor(text_region_np, cv2.COLOR_RGB2HSV)

    # Создаем маску на основе переданных границ цвета
    mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    yellow_ratio = np.sum(mask > 0) / (mask.shape[0] * mask.shape[1])
    print(yellow_ratio)
    return yellow_ratio > 0.5  # Если больше 50% области желтого цвета, считаем текст желтым


def extract_text_near_coin(image: Image.Image, coin_center: Tuple[int, int], lang: str = 'rus') -> str:
    """
    Извлекает текст рядом с центром найденной монетки.

    :param image: Скриншот экрана в формате PIL.
    :param coin_center: Координаты центра монетки в формате (x_center, y_center).
    :param lang: Язык для OCR (по умолчанию 'rus').
    :return: Извлеченный текст.
    """
    x_center, y_center = coin_center
    text_region = image.crop((x_center + 10, y_center - 20, x_center + 150, y_center + 20))

    extracted_text = pytesseract.image_to_string(text_region, lang=lang, config=config___oem_3__psm_6)
    return extracted_text.strip


def find_coin_and_check_text(
        template_name: str,
        lower_yellow: np.ndarray,
        upper_yellow: np.ndarray,
        region: Optional[Tuple[int, int, int, int]] = (0, 0, 1920, 1080)
) -> List[Tuple[int, int]]:
    """
    Ищет все монетки на экране и проверяет, является ли текст рядом с каждой из них заданного желтого цвета.

    :param template_name: Имя изображения-шаблона монетки.
    :param lower_yellow: Нижняя граница диапазона желтого цвета в HSV.
    :param upper_yellow: Верхняя граница диапазона желтого цвета в HSV.
    :param region: Регион экрана для захвата (по умолчанию захватывается весь экран).
    :return: Список координат центров монеток, если текст рядом с ними желтого цвета.
    """
    # Поиск всех монеток в регионе
    coin_centers = find_coin_in_region(template_name, region=region)

    if not coin_centers:
        print("Монетки не найдены.")
        return []

    # Захват экрана для дальнейшего анализа
    with mss.mss() as screen_capturer:
        screenshot = screen_capturer.grab(region) if region else screen_capturer.grab(screen_capturer.monitors[1])
        image = Image.frombytes('RGB', screenshot.size, screenshot.rgb)

    valid_coin_centers = []

    # Проверяем текст рядом с каждой монеткой
    for coin_center in coin_centers:
        if is_text_yellow(image, coin_center, lower_yellow, upper_yellow):
            valid_coin_centers.append(coin_center)

    return valid_coin_centers

def get_hsv_bounds(colors: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Получает нижнюю и верхнюю границы цвета в HSV на основе списка цветов в формате RGB.

    :param colors: NumPy массив цветов в формате RGB (shape: Nx3).
    :return: Нижняя и верхняя границы цвета в HSV.
    """
    colors = colors.astype(np.uint8)

    # Преобразуем RGB цвета в HSV
    colors_hsv = cv2.cvtColor(colors.reshape(1, -1, 3), cv2.COLOR_RGB2HSV)

    # Найдем минимальные и максимальные значения по каждому каналу (H, S, V)
    lower_bound = np.min(colors_hsv, axis=1)[0]
    upper_bound = np.max(colors_hsv, axis=1)[0]

    return lower_bound, upper_bound


def find_coin_in_region(
        template_name: str, region: Tuple[int, int, int, int] = (0, 0, 1920, 1080),
        threshold: float = 0.92, template_path: Optional[str] = "Images/") -> List[Tuple[int, int]]:
    """
    Поиск всех цветных шаблонов в указанной области экрана.

    :param template_name: Название изображения-шаблона, который нужно найти.
    :param region: Регион экрана в диапазоне (x1, y1, x2, y2).
    :param threshold: Порог совпадения (значение от 0 до 1), выше которого считается, что шаблон найден.
    :param template_path: Путь к директории, где находится изображение-шаблон.
    :return: Список координат верхнего левого угла найденных фрагментов или пустой список, если шаблоны не найдены.
    """
    template_full_path = f"{template_path}{template_name}.png"

    # Захватываем регион экрана
    (x1, y1, x2, y2) = region
    screenshot = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))

    # Загружаем шаблон в цвете (RGB)
    template = cv2.imread(template_full_path, cv2.IMREAD_COLOR)

    if template is None:
        raise FileNotFoundError(f"Template image not found: {template_full_path}")

    # Поиск всех совпадений на цветном изображении
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)

    # Получаем координаты всех найденных совпадений
    matches = []
    template_height, template_width = template.shape[:2]

    for point in zip(*locations[::-1]):  # Инвертируем координаты
        top_left = (point[0] + region[0], point[1] + region[1])
        matches.append(top_left)

    return matches
