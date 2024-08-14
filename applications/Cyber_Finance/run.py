from applications import *
from applications.Cyber_Finance import *
from modules.moves import Close_AnyWay
from modules.screens import hunt_for_the_button_in_list


def Run_Cyber_Finance(dailik):
    PreRun(find_Cyber_Finance, chat=True, chat_type="click", chatbot_string=2)
    pg.click(claim_Cyber_Finance)
    delay(0.4, 0.8)
    for coordinates in upgrade_egg_hummer:
        pg.click(coordinates)
        delay(0.4, 0.6)
    hunt_for_the_button_in_list(hummer_close)
    Close_AnyWay()
