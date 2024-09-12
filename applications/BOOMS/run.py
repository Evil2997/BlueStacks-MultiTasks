from applications import *
from applications.BOOMS import *
from modules.moves import Close_AnyWay


def Run_BOOMS(dailik, event, win_main):
    find_BOOMS = find_BOOMS_2 if win_main else find_BOOMS_1
    clicks_cycle_numeric = 2

    PreRun(find_BOOMS, win_main, initial_setup_clicker=True, initial_setup_images=pre_run_clicker)

    # if dailik:
    for coordinates in open_daily:
        pg.click(coordinates)
        delay(0.4, 1)
    delay(3, 4)
    for _ in range(clicks_cycle_numeric):
        pg.press('num4')
        delay(8, 12)
        pg.press('num4')
        delay(0.4, 0.6)
    Close_AnyWay()
