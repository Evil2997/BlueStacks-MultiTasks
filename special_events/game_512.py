import random

import pyautogui as pg

from modules.Timers import delay
from modules.moves import swipe_right, drag_to_up
from modules.screens import find_it_and_click_it
from special_events import *


def play_512(how_much_you_want_to_play):
    for game in range(how_much_you_want_to_play):
        delay(3, 4)
        drag_to_up(duration=0.4)
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
    delay(3, 4)


def random_moves():
    moves = ["up", "down", "left", "right"]
    move = random.choice(moves)
    return move
