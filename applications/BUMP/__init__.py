import os

import cv2
import numpy as np
import pyautogui as pg

from modules.Timers import delay

click_at_moon = ["click_at_moon"]

open_bust = (940, 800)
bust_activate = [(940, 720), (940, 950)]

find_BUMP = ["BUMP"]
green_X = ["green_X"]
gray_X = ["gray_X"]


def scan_BUMP_daily_reward(region=(0, 0, 1920, 1080)):
    (x1, y1, x2, y2) = region
    screenshot = np.array(pg.screenshot(region=(x1, y1, x2 - x1, y2 - y1)))

    tolerance = 3
    TARGET_COLORS = [(31, 125, 63)]
    for target_color in TARGET_COLORS:
        lower_bound = np.array([c - tolerance for c in target_color])
        upper_bound = np.array([c + tolerance for c in target_color])
        mask = cv2.inRange(screenshot, lower_bound, upper_bound)
        cv2.imwrite("1.png", mask)

    image = cv2.imread("1.png", cv2.IMREAD_GRAYSCALE)
    os.remove("1.png")
    white_pixels = np.column_stack(np.where(image == 255))
    if len(white_pixels) > 100:
        center_x = int(np.mean(white_pixels[:, 1]))
        center_y = int(np.mean(white_pixels[:, 0]))
        pg.click(center_x, center_y)
        delay()
