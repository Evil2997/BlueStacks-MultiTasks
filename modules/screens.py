import os
import time
from typing import Optional, Tuple

import cv2
import numpy as np
import pyautogui as pg
from PIL import ImageGrab
from pytesseract import pytesseract

from modules import *
from modules.Timers import delay


def get_image_size(image_name):
    image_path = f"Images/{image_name}.png"
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    height, width, _ = image.shape
    return width, height


def find_template_in_region(
        template_name: str, region: Tuple[int, int, int, int] = (0, 0, 1920, 1080),
        threshold: float = 0.92, template_path: Optional[str] = "Images/") -> Optional[Tuple[int, int]]:
    """
    Поиск шаблона в указанной области экрана.

    :param template_name: Название изображения-шаблона, который нужно найти.
    :param region: Регион экрана в диапазоне (x1, y1, x2, y2).
    :param threshold: Порог совпадения (значение от 0 до 1), выше которого считается, что шаблон найден.
    :param template_path: Путь к директории, где находится изображение-шаблон.
    :return: Координаты верхнего левого угла найденного фрагмента или None, если шаблон не найден.
    """
    template_full_path = f"{template_path}{template_name}.png"

    (x1, y1, x2, y2) = region
    screenshot = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))  # Захватываем регион экрана
    template = cv2.imread(template_full_path, cv2.IMREAD_GRAYSCALE)

    if template is None:
        raise FileNotFoundError(f"Template image not found: {template_full_path}")

    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)  # Преобразуем скриншот в grayscale

    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        top_left = (max_loc[0] + region[0], max_loc[1] + region[1])  # Корректируем координаты для всей области экрана
        return top_left

    return None


def find_it_and_click_it(name_list: list[str], region=(0, 0, 1920, 1080), threshold=0.92):
    for name in name_list:
        top_left = find_template_in_region(name, region, threshold=threshold)
        width, height = get_image_size(name)
        if top_left:
            delay(0.2, 0.3)
            pg.click(top_left[0] + width / 2, top_left[1] + height / 2)
            if len(name_list) == 1:
                return True
        elif len(name_list) == 1:
            return False


def hunt_for_the_button_in_list(name_list: list[str], hunt_in_seconds=10, region=(0, 0, 1920, 1080)):
    for name in name_list:
        time_start = time.time()
        while time.time() - time_start < hunt_in_seconds:
            top_left = find_template_in_region(name, region)
            width, height = get_image_size(name)
            if top_left:
                delay(0.2, 0.3)
                pg.click(top_left[0] + width / 2, top_left[1] + height / 2)
            else:
                delay(0.01, 0.1)


def cycle_hunter_click(name_list: list[str], region=(0, 0, 1920, 1080)):
    for name in name_list:
        while True:
            top_left = find_template_in_region(name, region)
            width, height = get_image_size(name)
            if top_left:
                delay(0.2, 0.3)
                pg.click(top_left[0] + width / 2, top_left[1] + height / 2)
                break
            else:
                delay(0.04, 0.2)
        delay(0.8, 1.2)


def click_on_images(target_colors, region=(0, 0, 1920, 1080), pixel_threshold=300):
    (x1, y1, x2, y2) = region
    screenshot = np.array(pg.screenshot(region=(x1, y1, x2 - x1, y2 - y1)))

    final_mask = np.zeros((screenshot.shape[0], screenshot.shape[1]), dtype=np.uint8)

    tolerance = 3
    for color in target_colors:
        lower_bound = np.array([c - tolerance for c in color])
        upper_bound = np.array([c + tolerance for c in color])
        mask = cv2.inRange(screenshot, lower_bound, upper_bound)
        final_mask = cv2.bitwise_or(final_mask, mask)

    cv2.imwrite("1.png", final_mask)

    image = cv2.imread("1.png", cv2.IMREAD_GRAYSCALE)
    os.remove("1.png")
    white_pixels = np.column_stack(np.where(image == 255))

    if len(white_pixels) > pixel_threshold:
        center_x = int(np.mean(white_pixels[:, 1]))
        center_y = int(np.mean(white_pixels[:, 0]))
        pg.click(center_x, center_y)
        return True
    else:
        return False


def found_text_on_image(region):
    screenshot = pg.screenshot(region=region)
    text = pytesseract.image_to_string(screenshot, config=config)
    return text


def fff(name, region=(0, 0, 1920, 1080), threshold=0.92):
    top_left = find_template_in_region(Image_Name=name, region=region, threshold=threshold)
    width, height = get_image_size(name)
    if top_left:
        region_image_founded = (top_left[0], top_left[1], top_left[0] + width, top_left[1] + height)
        text = found_text_on_image(region_image_founded)
        print(text)
