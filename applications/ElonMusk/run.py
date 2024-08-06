from applications import *
from applications.ElonMusk import *
from modules.moves import Close_AnyWay


def Run_ElonMusk(dailik):
    PreRun(find_ElonMusk)
    pg.click(Musk_take)
    delay(4, 5)
    if dailik:
        for coordinate in Elon_daily:
            pg.click(coordinate)
            delay(4, 5)
    Close_AnyWay()
