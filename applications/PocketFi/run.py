from applications import *
from applications.PocketFi import *
from modules.moves import Close_AnyWay


def Run_PocketFi(dailik):
    PreRun(find_PocketFi, threshold=0.7)
    for coordinates in mining_fi:
        pg.click(coordinates)
        delay()
    if dailik:
        for coordinates in get_daily_FiReward:
            pg.click(coordinates)
            delay(0.4, 1)
    pg.click(claim_switch)
    Close_AnyWay()
