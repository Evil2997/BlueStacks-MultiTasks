from applications import *
from applications.BEE import *
from modules.moves import Close_AnyWay
from modules.screens import click_on_images


def Run_BEE(dailik, event, win_main):
    find_BEE = find_BEE_2 if win_main else find_BEE_1
    PreRun(find_BEE, chat=True, chat_type="click", chatbot_string=2)
    if click_on_images(target_colors=colors_check_daily):
        pg.click(daily_BEE)
        delay()
    pg.click(upgrades_BEE)
    delay()
    for _ in range(3):
        drag_to_bottom(duration=0.2)
        delay(0.2, 0.3)
    for _ in range(20):
        for coordinates in upgrades_all:
            pg.click(coordinates)
            delay(0.02, 0.2)
        delay(0.25, 0.5)
    pg.click(other_menu_BEE)
    delay(3, 4)
    pg.click(upgrades_BEE)
    for _ in range(30):
        pg.click(upgrades_last)
        delay(0.6, 0.8)
    Close_AnyWay()
