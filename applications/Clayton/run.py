import random

from applications import *
from applications.Clayton import *
from modules.moves import Close_AnyWay, swipe_right


def play_512(how_much_you_want_to_play):
    for game in range(how_much_you_want_to_play):
        pg.click(go_to_games)
        delay()
        for _ in range(4):
            drag_to_up()
        pg.click(button_play_512)
        delay()
        for i in range(1024):
            pg.press(random_moves())
            if i % 10 == 0:
                if find_template_in_region(next_game_clayton, threshold=0.86):
                    delay(3, 4)
                    for _ in range(4):
                        pg.click(get_reward_clayton_game)
                        delay(0.02, 0.1)
                    delay(3, 4)
                    for _ in range(4):
                        pg.click(next_game_play)
                        delay(0.02, 0.1)
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
    pg.click(claim_daily_reward)
    delay()
    for _ in range(4):
        find_it_and_click_it(clayton_lvl_up)

    # play_512(how_much_you_want_to_play)
    Close_AnyWay()
