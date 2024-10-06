import os
from typing import Dict
from typing import Optional, Tuple

import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageGrab

from modules import config___oem_3__psm_11


def extract_text_and_coordinates(image: Image.Image, lang: str = 'rus') -> Dict[str, Dict[int, Tuple[int, int]]]:
    """
    Извлекает текст и его координаты из изображения с помощью Tesseract OCR.

    :param image: Изображение, из которого нужно извлечь текст.
    :param lang: Язык для OCR (по умолчанию 'rus').
    :return: Словарь с данными, где ключ - текст, а значение - словарь индексов и координат.
    """
    ocr_data = pytesseract.image_to_data(image, lang=lang, config=config___oem_3__psm_11,
                                         output_type=pytesseract.Output.DICT)

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
    img = ImageGrab.grab(bbox=region)  # Захват области
    coordinates = extract_text_and_coordinates(img, lang)

    if target_phrase in coordinates:
        x, y = list(coordinates[target_phrase].values())[occurrence_index]
        return x, y
    return None
