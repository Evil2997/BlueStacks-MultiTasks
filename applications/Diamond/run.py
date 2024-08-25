from applications import *
from applications.Diamond import *
from modules.moves import Close_AnyWay


def Old_Run_Diamond(dailik):
    PreRun(find_Diamond)
    for i in [0, 1]:
        pg.press("num4")
        delay(12, 14)
        pg.press("num4")
        delay()
        pg.click(get_diamonds_reward_from_game)
        delay()
        if i == 0:
            pg.click(get_diamonds_reward_from_game)
            delay(18, 20)
    if dailik:
        for coordinates in diamond_daily_reward:
            pg.click(coordinates)
            delay()
    Close_AnyWay()


def Run_Diamond(dailik, event, win_main):
    find_Diamond = find_Diamond_2 if win_main else find_Diamond_1

    PreRun(find_Diamond)
    if dailik:
        for coordinates in diamond_daily_reward:
            pg.click(coordinates)
            delay()
    for _ in range(8):
        if find_it_and_click_it(diamond_tap_to_start_game):
            pg.press("num4")
            for _ in range(1024):
                if find_it_and_click_it(get_reward_diamond):
                    pg.press("num4")
                    delay()
                    find_it_and_click_it(get_reward_diamond)
                    break
                else:
                    delay(0.02, 0.2)
            # else:
            #     pg.press("num4")
            # [Watch_ADS]-[Start]
            delay()
            if find_it_and_click_it(diamond_watch_ads):
                pg.click(get_diamonds_reward_from_game)
                delay(18, 20)
            else:
                break
            # [Watch_ADS]-[End]
    # [Upgrades]-[Start]
    pg.click(open_upgrades)
    delay()
    pg.click(grade_1)
    delay()
    pg.click(grade_2)
    delay()
    # [Upgrades]-[End]
    Close_AnyWay()
