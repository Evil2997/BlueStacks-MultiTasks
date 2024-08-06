from applications import *
from applications.Diamond import *
from modules.moves import Close_AnyWay


def Run_Diamond(dailik):
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
