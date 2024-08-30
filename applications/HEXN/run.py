from applications import *
from applications.HEXN import *
from modules.moves import Close_AnyWay


def Run_HEXN(dailik, event, win_main):
    find_HEXN = find_HEXN_2 if win_main else find_HEXN_1

    PreRun(find_HEXN, win_main)
    for coordinates in claim_reward_HEXN:
        pg.click(coordinates)
        delay(2, 3)
    # rocket()
    Close_AnyWay()


def rocket():
    for coordinates in rocket_time_reward:
        pg.click(coordinates)
        delay(0.4, 0.6)
