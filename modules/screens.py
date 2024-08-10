import os
import time

import cv2
import numpy as np
import pyautogui as pg
from PIL import ImageGrab

from modules.Timers import delay


def get_image_size(image_name):
    image_path = f"Images/{image_name}.png"
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    height, width, _ = image.shape
    return width, height


def find_template_on_region(Image_Name, region=(0, 0, 1920, 1080), threshold=0.92):
    """
    Поиск фрагмента в нужном регионе экрана
    :param region: регион экрана в диапазоне (0, 0, 1920, 1080)
    :param Image_Name: Название изображения которое будем искать
    :return: Верхний левый угол найденного фрагмента
    """
    template_path = f"Images/{Image_Name}.png"
    (x1, y1, x2, y2) = region
    screenshot = np.array(ImageGrab.grab(bbox=(x1, y1, x2 - x1, y2 - y1)))
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        raise FileNotFoundError(f"Template image not found: {template_path}")

    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        top_left = (max_loc[0] + region[0], max_loc[1] + region[1])
    else:
        top_left = None
    return top_left


def find_it_and_click_it(name_list: list[str], region=(0, 0, 1920, 1080), threshold=0.92):
    for name in name_list:
        top_left = find_template_on_region(name, region, threshold=threshold)
        width, height = get_image_size(name)
        if top_left:
            delay(0.2, 0.3)
            pg.click(top_left[0] + width / 2, top_left[1] + height / 2)
            return True
        elif len(name_list) == 1:
            return False


def hunt_for_the_button_in_list(name_list: list[str], hunt_in_seconds=10, region=(0, 0, 1920, 1080)):
    for name in name_list:
        time_start = time.time()
        while time.time() - time_start < hunt_in_seconds:
            top_left = find_template_on_region(name, region)
            width, height = get_image_size(name)
            if top_left:
                delay(0.2, 0.3)
                pg.click(top_left[0] + width / 2, top_left[1] + height / 2)
                return True
            else:
                delay(0.01, 0.1)
        else:
            if len(name_list) == 1:
                return False


def cycle_hunter_click(name_list: list[str], region=(0, 0, 1920, 1080)):
    for name in name_list:
        while True:
            top_left = find_template_on_region(name, region)
            width, height = get_image_size(name)
            if top_left:
                delay(0.2, 0.3)
                pg.click(top_left[0] + width / 2, top_left[1] + height / 2)
                break
            else:
                delay(0.01, 0.08)
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
    print(len(white_pixels))
    if len(white_pixels) > pixel_threshold:
        center_x = int(np.mean(white_pixels[:, 1]))
        center_y = int(np.mean(white_pixels[:, 0]))
        pg.click(center_x, center_y)
        delay()
        return True
    else:
        return False
