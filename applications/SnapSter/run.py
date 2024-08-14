from applications import *
from applications.SnapSter import *
from modules.moves import Close_AnyWay


def Run_SnapSter(dailik):
    PreRun(find_SnapSter, chat=True, chat_type="click", chatbot_string=1)
    pg.click(SnapSter_claim_and_farm)
    delay(0.4, 0.6)
    Close_AnyWay()
