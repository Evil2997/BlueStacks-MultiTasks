from applications import *
from applications.Baboon import *
from modules.moves import Close_AnyWay


def Run_Baboon(dailik):
    PreRun(find_Baboon, chat=True, chat_type="click", chatbot_string=0)
    if dailik:
        for coordinates in Baboon_daily_reward:
            pg.click(coordinates)
            delay(0.4, 0.8)
        for battery in combo_battery:
            pg.click(battery)
            delay(0.4, 0.8)
        pg.press("Esc")
        delay()
    for _ in range(4):
        pg.press("num4")
        delay(25, 30)
        pg.press("num4")
        delay()
        for coordinates in repair_battery:
            pg.click(coordinates)
            delay()
    for coordinates in upgrade_battery:
        pg.click(coordinates)
        delay()
    Close_AnyWay()
