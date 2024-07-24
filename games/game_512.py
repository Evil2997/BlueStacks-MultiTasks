import random

import pyautogui as pg

from games import *
from modules.Timers import delay
from modules.moves import drag_to_bottom, swipe_right
from modules.screens import find_it_and_click_it


def play_512(how_much_you_want_to_play):
    for game in range(how_much_you_want_to_play):
        delay(3, 4)
        drag_to_bottom()
        delay()
        swipe_right()
        delay()
        pg.click(button_play_512)
        delay(6, 7)
        for i in range(65536):
            pg.press(random_moves())
            if i % 10 == 0:
                if find_it_and_click_it(main_menu):
                    delay()
                    find_it_and_click_it(main_menu)
                    break


def random_moves():
    moves = ["up", "down", "left", "right"]
    move = random.choice(moves)
    return move
