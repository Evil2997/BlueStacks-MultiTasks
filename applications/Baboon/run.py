from applications import *
from applications.Baboon import *
from modules.moves import Close_AnyWay


def Run_Baboon(dailik, event, win_main):
    find_Baboon = find_Baboon_2 if win_main else find_Baboon_1

    PreRun(find_Baboon, win_main, chat=True, chat_type="click", chatbot_string=0)

    if dailik:
        for coordinates in Baboon_daily_reward:
            pg.click(coordinates)
            delay(0.8, 1)
        for battery in combo_battery:
            pg.click(battery)
            delay(0.8, 1)
        pg.press("Esc")
        delay()
    for _ in range(32):
        pg.press("num4")
        delay(10, 15)
        pg.press("num4")
        delay(0.8, 1)
        for coordinates in repair_battery:
            pg.click(coordinates)
            delay(0.8, 1)
    for coordinates in upgrade_battery:
        pg.click(coordinates)
        delay()
    Close_AnyWay()
