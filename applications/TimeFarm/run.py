from applications import *
from applications.TimeFarm import *
from modules.moves import Close_AnyWay


def Run_TimeFarm(dailik, event):
    PreRun(find_TimeFarm, chat=True, chat_type="click", chatbot_string=1)
    for coordinates in FarmingTime:
        pg.click(coordinates)
        delay(6, 8)
    Close_AnyWay()
