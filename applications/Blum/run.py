from applications import *
from applications.Blum import *
from modules.moves import Close_AnyWay


def Run_Blum(dailik, event, win_main):
    find_Blum = find_Blum_2 if win_main else find_Blum_1

    PreRun(find_Blum, win_main)

    for _ in range(2):
        pg.click(claim_reward_daily)
        delay()
        for _ in range(3):
            pg.click(claim_farm)
            delay()
        Close_AnyWay()
