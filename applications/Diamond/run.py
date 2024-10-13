import time

from applications import *
from applications.Diamond import *
from modules.moves import Close_AnyWay


def Run_Diamond(dailik, event, win_main):
    find_Diamond = find_Diamond_2 if win_main else find_Diamond_1

    PreRun(find_Diamond, win_main)

    if find_it_and_click_it(diamond_claim_prerun):
        delay(0.2, 0.4)

    if dailik:
        make_dailik()
    cycle_clicker_at_diamond()
    delay()
    make_upgrades()
    Close_AnyWay()


def make_upgrades():
    pg.click(open_upgrades)
    delay(0.2, 0.4)
    for _ in range(2):
        pg.click(grade_1)
        delay(0.2, 0.4)
        pg.click(grade_2)
        delay(0.2, 0.4)


def make_dailik():
    for coordinates in diamond_daily_reward:
        pg.click(coordinates)
        delay()


def cycle_clicker_at_diamond():
    for _ in range(8):
        if find_it_and_click_it(diamond_tap_to_start_game_list):
            pg.press("num4")
            for _ in range(1024):
                if find_it_and_click_it(get_reward_diamond, threshold=0.88):
                    pg.press("num4")
                    delay()
                    find_it_and_click_it(get_reward_diamond)
                    break
                delay(0.04, 0.2)
            # [Watch_ADS]-[Start]
            delay(0.04, 0.2)
            if find_template_in_region(diamond_watch_ads):
                delay(3, 4)
                pg.click(get_diamonds_reward_from_game)
                time_start = time.time()
                while time.time() - time_start <= 32:
                    if find_template_in_region(diamond_tap_to_start_game_str):
                        break
                    delay(0.04, 0.2)
            # [Watch_ADS]-[End]