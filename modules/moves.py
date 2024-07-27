import random

import pyautogui as pg

from modules.Timers import delay
from modules.screens import find_it_and_click_it, find_template_on_region

cords_to_drag = (1700, 300)
cords_close = (116, 132)
cords_to_swipe = (700, 750)

close_anyway = ["close_anyway"]


def drag_to_up(duration=0.2):
    random_y = random.uniform(-15, 15)
    pg.moveTo(cords_to_drag[0], cords_to_drag[1])
    pg.dragTo(cords_to_drag[0], cords_to_drag[1] + random_y + 295, duration=duration)
    pg.mouseUp()


def drag_to_bottom(duration=0.2):
    random_y = random.uniform(-15, 15)
    pg.moveTo(cords_to_drag[0], cords_to_drag[1] + random_y + 495)
    pg.dragTo(cords_to_drag[0], cords_to_drag[1], duration=duration)
    pg.mouseUp()


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
