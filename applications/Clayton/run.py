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
        for i in range(1024):
            pg.press(random_moves())
            if i % 10 == 0:
                if find_it_and_click_it(main_menu_Clayton_game):
                    delay()
                    find_it_and_click_it(main_menu_Clayton_game)
                    delay()
                    find_it_and_click_it(clayton_lvl_up)
                    break
    delay(3, 4)


def random_moves():
    moves = ["up", "down", "left", "right"]
    move = random.choice(moves)
    return move


def Run_Clayton(dailik, event, win_main):
    find_Clayton = find_Clayton_2 if win_main else find_Clayton_1
    how_much_you_want_to_play = 4

    PreRun(find_Clayton, win_main)

    pg.click(clayton_pre_game_ads)
    delay()
    if dailik:
        pg.click(claim_daily_reward)
        delay()
        for _ in range(4):
            find_it_and_click_it(clayton_lvl_up)
    drag_to_bottom(duration=0.4)
    for _ in range(4):
        pg.click(claim_coins)
        delay(0.6, 1)
        for _ in range (4):
            find_it_and_click_it(clayton_lvl_up)
    play_512(how_much_you_want_to_play)
    Close_AnyWay()
