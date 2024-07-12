import random

import pyautogui as pg

from modules.screens import find_it_and_click_it, find_template_on_region
from modules.time import delay

cords_to_drag = (1700, 430)
cords_to_start_drag = (1650, 830)
cords_close = (116, 132)

close_anyway = ["close_anyway"]


def drag_to_up():
    delay(0.02, 0.06)
    random_x = random.uniform(-20, 20)
    random_y = random.uniform(-20, 20)
    pg.moveTo(cords_to_drag[0] + random_x, cords_to_drag[1] + random_y, duration=0.1)
    pg.mouseDown()
    pg.moveTo(cords_to_drag[0] + random_x, cords_to_drag[1] + random_y + 310, 0.4)
    pg.mouseUp()


def drag_to_bottom():
    delay(0.02, 0.1)
    pg.moveTo(cords_to_start_drag, duration=0.06)
    pg.dragTo(cords_to_drag, duration=0.12)


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


def move_mouse(start, end):
    pg.mouseUp()
    pg.moveTo(start)
    pg.mouseDown()
    pg.moveTo(end)
    pg.mouseUp()


# def random_moves_clayton():
#     start_end_pairs = [(moves[1], moves[0]), (moves[0], moves[1]), (moves[3], moves[2]), (moves[2], moves[3])]
#     start, end = random.choice(start_end_pairs)
#     move_mouse(start, end)
#
#
# Список координат (up, down, left, right)
# moves = [(), (), (), ()]
# for _ in range(10):
#     random_moves_clayton()
#     delay(0.02, 0.1)