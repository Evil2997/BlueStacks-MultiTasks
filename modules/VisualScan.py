from typing import List, Dict, Tuple, Optional
import mss
import pyautogui as pg
import pytesseract
from PIL import Image


def capture_full_screen_or_region(region: Optional[Tuple[int, int, int, int]] = None) -> Image.Image:
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


def extract_text_and_coordinates(image: Image.Image, lang: str = 'rus') -> Dict[str, List]:
    """
    Извлекает текст и его координаты из изображения с помощью Tesseract OCR.

    :param image: Изображение, из которого нужно извлечь текст.
    :param lang: Язык для OCR (по умолчанию 'rus').
    :return: Словарь с данными, содержащими текст и соответствующие координаты.
    """
    custom_config = r'--oem 3 --psm 6'
    ocr_data = pytesseract.image_to_data(image, lang=lang, config=custom_config, output_type=pytesseract.Output.DICT)
    return ocr_data


def find_target_phrases_coordinates(ocr_data: Dict[str, List], target_phrases: List[str]) -> Dict[str, List[Tuple[int, int]]]:
    """
    Находит координаты целевых фраз на изображении.

    :param ocr_data: Данные OCR, содержащие текст и координаты.
    :param target_phrases: Список целевых фраз для поиска.
    :return: Словарь с координатами (центральными точками) для каждой найденной целевой фразы.
    """
    coordinates = {}
    for i in range(len(ocr_data['text'])):
        text = ocr_data['text'][i].strip()
        if text in target_phrases:
            x, y, w, h = ocr_data['left'][i], ocr_data['top'][i], ocr_data['width'][i], ocr_data['height'][i]
            x_center, y_center = x + w // 2, y + h // 2
            if text not in coordinates:
                coordinates[text] = []
            coordinates[text].append((x_center, y_center))
    return coordinates


def scan_screen_and_find_phrases_coordinates(
        region: Optional[Tuple[int, int, int, int]] = None,
        lang: str = 'rus',
        target_phrases: Optional[List[str]] = None) -> Dict[str, List[Tuple[int, int]]]:
    """
    Сканирует экран, извлекает текст и находит координаты целевых фраз.

    :param region: Область для захвата (если None, захватывается весь экран).
    :param lang: Язык для OCR (по умолчанию 'rus').
    :param target_phrases: Список целевых фраз для поиска.
    :return: Словарь с координатами найденных фраз.
    """
    img = capture_full_screen_or_region(region)
    ocr_data = extract_text_and_coordinates(img, lang)
    return find_target_phrases_coordinates(ocr_data, target_phrases)


def visual_scan_tracker(region: Optional[Tuple[int, int, int, int]] = None,
                                       lang: str = 'rus',
                                       target_phrases: Optional[List[str]] = None) -> Optional[Tuple[int, int]]:
    """
    Сканирует экран, находит целевые фразы и возвращает координаты первой найденной фразы.

    :param region: Область для захвата (если None, захватывается весь экран).
    :param lang: Язык для OCR (по умолчанию 'rus').
    :param target_phrases: Список целевых фраз для поиска.
    :return: Координаты (x, y) первой найденной фразы или None, если фразы не найдены.
    """
    coordinates = scan_screen_and_find_phrases_coordinates(region=region, lang=lang, target_phrases=target_phrases)
    for phrase, cords_list in coordinates.items():
        for idx, (x, y) in enumerate(cords_list):
            print(f"Найдена фраза '{phrase}' [{idx}] на координатах: ({x}, {y})")
            return (x, y)
    return None
