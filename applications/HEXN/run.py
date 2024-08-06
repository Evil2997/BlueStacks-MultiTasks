from applications import *
from applications.HEXN import *
from modules.moves import Close_AnyWay


def Run_HEXN(dailik):
    PreRun(find_HEXN)
    for coordinates in claim_reward_HEXN:
        pg.click(coordinates)
        delay(6, 8)
    for coordinates in rocket_time_reward:
        pg.click(coordinates)
        delay(0.4, 0.6)
    Close_AnyWay()
