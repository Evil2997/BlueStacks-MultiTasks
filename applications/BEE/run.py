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
        for coordinates in upgrades_BEE:
            pg.click(coordinates)
            delay(0.01, 0.1)
        delay(4, 5)
        if i == 0:
            for _ in range(3):
                drag_to_bottom(duration=0.33)
                delay()
        for _ in range(40):
            if click_on_images(target_colors=colors_upgrades):
                delay(0.2, 0.4)
        if i == 0:
            pg.press('Esc')

    Close_AnyWay()
