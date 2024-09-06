import random

import pyautogui as pg

from modules import *
from modules.Timers import delay
from modules.screens import find_it_and_click_it, find_template_in_region


def drag_to_up(duration=0.16, cords_to_drag=cords_to_drag):
    random_y = random.uniform(-15, 15)
    pg.moveTo(cords_to_drag[0], cords_to_drag[1])
    pg.dragTo(cords_to_drag[0], cords_to_drag[1] + random_y + 295, duration=duration)


def drag_to_bottom(duration=0.16, cords_to_drag=cords_to_drag):
    random_y = random.uniform(-15, 15)
    pg.moveTo(cords_to_drag[0], cords_to_drag[1] + random_y + 345)
    pg.dragTo(cords_to_drag[0], cords_to_drag[1], duration=duration)


def Close_AnyWay(times_to_click=8):
    for _ in range(times_to_click):
        if find_template_in_region(telegram_account_settings):
            break
        delay(2, 3)
        pg.click(cords_close)
        delay()
        find_it_and_click_it(close_anyway)


def swipe_right(duration=0.2):
    pg.moveTo(cords_to_swipe[0], cords_to_swipe[1])
    pg.dragTo(cords_to_swipe[0] + 800, cords_to_swipe[1], duration=duration)
    pg.mouseUp()


def swipe_left(duration=0.2):
    pg.moveTo(cords_to_swipe[0] + 1000, cords_to_swipe[1])
    pg.dragTo(cords_to_swipe[0] - 600, cords_to_swipe[1], duration=duration)
    pg.mouseUp()
