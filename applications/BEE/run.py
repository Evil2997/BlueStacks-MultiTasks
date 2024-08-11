from applications import *
from applications.BEE import *
from modules.moves import Close_AnyWay
from modules.screens import click_on_images


def Run_BEE(dailik):
    PreRun(find_BEE, chat=True, chat_type="click", chatbot_string=2)
    # dailik
    if click_on_images(target_colors=colors_check_daily):
        pg.click(daily_BEE)
        delay(3, 4)

    for i in [0, 1]:
        pg.click(upgrades_BEE)
        delay(3, 4)
        if i == 0:
            for _ in range(3):
                drag_to_bottom(duration=0.2)
                delay()
        for _ in range(40):
            click_on_images(target_colors=colors_upgrades)
        if i == 0:
            pg.click(other_menu_BEE)
    Close_AnyWay()
