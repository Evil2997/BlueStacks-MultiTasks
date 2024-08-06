import random

import pyautogui as pg

from modules import *
from modules.Timers import delay
from modules.screens import find_it_and_click_it, find_template_on_region


def drag_to_up(duration=0.12, cords_to_drag=cords_to_drag):
    random_y = random.uniform(-15, 15)
    pg.moveTo(cords_to_drag[0], cords_to_drag[1])
    pg.dragTo(cords_to_drag[0], cords_to_drag[1] + random_y + 295, duration=duration)


def drag_to_bottom(duration=0.12, cords_to_drag=cords_to_drag):
    random_y = random.uniform(-15, 15)
    pg.moveTo(cords_to_drag[0], cords_to_drag[1] + random_y + 495)
    pg.dragTo(cords_to_drag[0], cords_to_drag[1], duration=duration)


def Close_AnyWay():
    telegram_account_settings = "telegram_account_settings"
    for _ in range(4):
        if find_template_on_region(telegram_account_settings):
            break
        delay(4, 5)
        pg.click(cords_close)
        delay(0.4, 0.6)
        find_it_and_click_it(close_anyway)
        delay(0.4, 0.6)


def swipe_right(duration=0.2):
    pg.moveTo(cords_to_swipe[0], cords_to_swipe[1])
    pg.dragTo(cords_to_swipe[0] + 800, cords_to_swipe[1], duration=duration)
    pg.mouseUp()


def swipe_left(duration=0.2):
    pg.moveTo(cords_to_swipe[0] + 600, cords_to_swipe[1])
    pg.dragTo(cords_to_swipe[0] - 300, cords_to_swipe[1], duration=duration)
    pg.mouseUp()
