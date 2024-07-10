import random

import pyautogui as pg

from modules.screens import find_it_and_click_it
from modules.time import delay

cords_to_drag = (1700, 430)
cords_to_start_drag = (1650, 830)
cords_close = (116, 132)

close_anyway = "close_anyway"


def drag_to_up():
    delay(0.02, 0.06)
    random_x = random.uniform(-20, 20)
    random_y = random.uniform(-20, 20)
    pg.moveTo(cords_to_drag[0] + random_x, cords_to_drag[1] + random_y, duration=0.1)
    pg.mouseDown()
    pg.moveTo(cords_to_drag[0] + random_x, cords_to_drag[1] + random_y + 310, 0.4)
    pg.mouseUp()


def drag_to_bottom():
    delay(0.04, 0.08)
    pg.moveTo(cords_to_start_drag, duration=0.06)
    pg.dragTo(cords_to_drag, duration=0.12)


def Close_AnyWay():
    for _ in range(2):
        delay(4, 5)
        pg.click(cords_close)
        delay(0.4, 0.6)
        find_it_and_click_it(close_anyway)
        delay(0.4, 0.6)
