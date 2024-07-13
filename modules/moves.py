import random

import pyautogui as pg

from modules.screens import find_it_and_click_it, find_template_on_region
from modules.Timers import delay

cords_to_drag = (1700, 430)
cords_to_start_drag = (1650, 830)
cords_close = (116, 132)

close_anyway = ["close_anyway"]


def drag_to_up():
    random_y = random.uniform(-25, 25)
    pg.mouseUp()
    pg.moveTo(cords_to_drag[0], cords_to_drag[1])
    pg.mouseDown()
    pg.moveTo(cords_to_drag[0], cords_to_drag[1] + random_y + 325, 0.16)
    pg.mouseUp()


def drag_to_bottom():
    pg.moveTo(cords_to_start_drag)
    pg.mouseDown()
    pg.moveTo(cords_to_drag, duration=0.06)
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
