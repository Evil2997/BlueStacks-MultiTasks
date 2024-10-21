from applications import *
from applications.BEE import *
from modules.Text_workers import fff
from modules.moves import Close_AnyWay
from modules.screens import click_in_center_on_region_by_color


def Run_BEE(dailik, event, win_main):
    find_BEE = find_BEE_2 if win_main else find_BEE_1

    PreRun(find_BEE, win_main, chat=True, chat_type="click", chatbot_string=2)

    get_dailik()
    upgrade_stage_1()
    upgrade_stage_2()
    Close_AnyWay()


def get_dailik():
    if click_in_center_on_region_by_color(target_colors=colors_check_daily):
        pg.click(daily_BEE)
        delay()


def upgrade_stage_1():
    pg.click(upgrades_BEE)
    delay()
    for _ in range(3):
        drag_to_bottom(duration=0.2)
        delay(0.2, 0.3)
    for coordinates in upgrades_all:
        for _ in range(10):
            pg.click(coordinates)
            delay(0.02, 0.2)
        delay(0.25, 0.5)


def upgrade_stage_2():
    pg.click(other_menu_BEE)
    delay()
    pg.click(upgrades_BEE)
    for _ in range(10):
        pg.click(upgrades_last)
        delay(0.02, 0.2)
