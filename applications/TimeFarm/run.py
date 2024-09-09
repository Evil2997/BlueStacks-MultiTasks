from applications import *
from applications.TimeFarm import *
from modules.moves import Close_AnyWay


def Run_TimeFarm(dailik, event, win_main):
    find_TimeFarm = find_TimeFarm_2 if win_main else find_TimeFarm_1

    PreRun(find_TimeFarm, win_main, chat=True, chat_type="click", chatbot_string=1)

    for coordinates in FarmingTime:
        pg.click(coordinates)
        delay(6, 8)
    hunt_for_the_button_in_list(TimeFarm_open_upgrade)
    for _ in range(4):
        for _ in range(2):
            if find_it_and_click_it(TimeFarm_make_upgrade):
                delay(0.6, 1)
                pg.click(agree_upgrade)
                delay(0.6, 1)
            drag_to_bottom()
        for _ in range(2):
            if find_it_and_click_it(TimeFarm_make_upgrade):
                delay(0.6, 1)
                pg.click(agree_upgrade)
                delay(0.6, 1)
            drag_to_up()
    Close_AnyWay()
