from applications import *
from applications.SnapSter import *
from modules.moves import Close_AnyWay


def Run_SnapSter(dailik, event, win_main):
    find_SnapSter = find_SnapSter_2 if win_main else find_SnapSter_1

    PreRun(find_SnapSter, win_main, chat=True, chat_type="click", chatbot_string=0)

    for coordinates in SnapSter_claim_and_farm:
        pg.click(coordinates)
        delay(0.4, 0.6)
    Close_AnyWay()
