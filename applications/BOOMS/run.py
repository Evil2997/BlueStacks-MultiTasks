from applications import *
from applications.BOOMS import *
from modules.moves import Close_AnyWay
from modules.screens import fff


def Run_BOOMS(dailik, event):
    PreRun(find_BOOMS)
    if dailik:
        for coordinates in open_daily:
            pg.click(coordinates)
            delay(0.4, 1)
        delay(3, 4)
    # fff()
    Close_AnyWay()







