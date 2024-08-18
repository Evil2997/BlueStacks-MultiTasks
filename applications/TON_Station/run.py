from applications import *
from applications.TON_Station import *
from modules.moves import Close_AnyWay


def Run_TON_Station(dailik):
    PreRun(find_TON_Station)
    for _ in range(2):
        pg.click(TON_Station_claim)
        delay(3, 4)
    pg.click(home_page)
    delay()
    for _ in range(2):
        pg.click(start_farm_and_claim_reward)
        delay(3, 4)
    Close_AnyWay()
