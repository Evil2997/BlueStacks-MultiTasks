from applications import *
from applications.BEE import *
from modules.moves import Close_AnyWay


def BEE_check_daily():
    pass


def Run_BEE(dailik):
    PreRun(find_BEE, chat=True, chat_type="click", chatbot_string=2)
    drag_to_bottom(duration=0.6)
    delay()
    # BEE_check_daily()
    pg.click(daily_BEE)
    delay(3, 4)
    for coordinates in upgrades_BEE:
        pg.click(coordinates)
        delay(0.01, 0.1)
    delay(8, 10)
    for _ in range(3):
        drag_to_bottom(duration=0.33)
        delay()
    for i, stage in enumerate(upgrades_BEE_stages):
        if i == 3:
            pg.click(other_menu_BEE)
            delay()
            for coordinates in upgrades_BEE:
                pg.click(coordinates)
                delay(0.01, 0.1)
            delay(4, 5)
        for _ in range(20):
            pg.click(stage)
            delay(0.6, 1)
    Close_AnyWay()
