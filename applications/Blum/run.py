from applications import *
from applications.Blum import *
from modules.moves import Close_AnyWay


def Run_Blum(dailik, event, win_main):
    find_Blum = find_Blum_2 if win_main else find_Blum_1

    PreRun(find_Blum, win_main)
    pg.click(claim_reward_daily)
    delay(3, 4)
    for _ in range(2):
        pg.click(claim_farm)
        delay(3, 4)
    Close_AnyWay()
