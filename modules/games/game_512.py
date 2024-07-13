import random
import time

import pyautogui as pg

from modules.Timers import delay
from modules.moves import drag_to_bottom
from modules.screens import hunt_for_the_button_in_list


def play_512(how_much_you_want_to_play):
    drag_to_bottom()
    hunt_for_the_button_in_list(Clayton_512_play)
    delay()
    for game in range(how_much_you_want_to_play):
        pg.click(Clayton_512_start)
        time_start = time.time()
        while time.time() - time_start <= 150:
            random_moves()
        hunt_for_the_button_in_list(take_reward_512)
    pg.click(Clayton_512_back)


def random_moves():
    moves = [(940, 470), (940, 850), (700, 650), (1170, 650)]
    start_end_pairs = [(moves[1], moves[0]), (moves[0], moves[1]), (moves[3], moves[2]), (moves[2], moves[3])]
    start, end = random.choice(start_end_pairs)
    move_mouse(start, end)


def move_mouse(start, end):
    pg.moveTo(start)
    pg.mouseDown()
    pg.moveTo(end)
    pg.mouseUp()


if __name__ == '__main__':
    Clayton_512_play = ["Clayton_512_play"]
    take_reward_512 = ["take_reward_512"]
    Clayton_512_start = (940, 780)
    Clayton_512_back = (940, 880)
