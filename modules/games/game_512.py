import random

import pyautogui as pg

from modules.Timers import delay
from modules.moves import drag_to_bottom
from modules.screens import hunt_for_the_button_in_list, find_it_and_click_it


def play_512(how_much_you_want_to_play):
    drag_to_bottom()
    hunt_for_the_button_in_list(Clayton_512_play)
    delay()
    for game in range(how_much_you_want_to_play):
        pg.click(Clayton_512_start)
        for i in range(65536):
            pg.press(random_moves())
            if i % 10 == 0:
                if find_it_and_click_it(take_reward_512):
                    break
        hunt_for_the_button_in_list(take_reward_512)
        delay()
    pg.click(Clayton_512_back)


def random_moves():
    moves = ["up", "down", "left", "right"]
    move = random.choice(moves)
    return move


Clayton_512_play = ["Clayton_512_play"]
take_reward_512 = ["take_reward_512"]
Clayton_512_start = (940, 780)
Clayton_512_back = (940, 880)
