from applications import *
from applications.TON_Station import *
from modules.moves import Close_AnyWay


def Run_TON_Station(dailik, event, win_main):
    find_TON_Station = find_TON_Station_2 if win_main else find_TON_Station_1

    PreRun(find_TON_Station, win_main)

    for _ in range(3):
        pg.click(TON_Station_claim)
        delay(3, 4)
    pg.click(home_page)
    delay()
    for _ in range(3):
        pg.click(start_farm_and_claim_reward)
        delay(3, 4)
    Close_AnyWay()
