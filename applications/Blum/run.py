from applications import *
from applications.Blum import *
from modules.moves import Close_AnyWay


def Run_Blum(dailik, event):
    PreRun(find_Blum)
    if dailik:
        pg.click(claim_reward_daily)
        delay(2, 3)
    for _ in range(2):
        pg.click(claim_farm)
        delay(2, 3)
    Close_AnyWay()
