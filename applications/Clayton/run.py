import random

from applications import *
from applications.Clayton import *
from modules.moves import Close_AnyWay, swipe_right


def play_512(how_much_you_want_to_play):
    for game in range(how_much_you_want_to_play):
        delay(3, 4)
        drag_to_bottom(duration=0.4)
        delay()
        swipe_right()
        delay()
        pg.click(button_play_512)
        delay(6, 7)
        for i in range(65536):
            pg.press(random_moves())
            if i % 10 == 0:
                if find_it_and_click_it(main_menu_Clayton_game):
                    delay()
                    find_it_and_click_it(main_menu_Clayton_game)
                    break
    delay(3, 4)


def random_moves():
    moves = ["up", "down", "left", "right"]
    move = random.choice(moves)
    return move


def Run_Clayton(dailik):
    how_much_you_want_to_play = 2
    PreRun(find_Clayton)
    if dailik:
        pg.click(claim_daily_reward)
        delay()
    drag_to_bottom(duration=0.4)
    for _ in range(4):
        pg.click(claim_coins)
        delay(0.5, 0.8)
    play_512(how_much_you_want_to_play)
    Close_AnyWay()
