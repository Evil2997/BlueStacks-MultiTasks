from applications import *
from applications.Time_TON_Ecosystem import *
from modules.moves import Close_AnyWay

def Run_Time_TON_Ecosystem(dailik):
    PreRun(find_Time_TON_Ecosystem, chat=True, chat_type="click", chatbot_string=2)
    if dailik:
        pg.click(daily_TON_Ecosystem)
    drag_to_bottom(duration=0.4)
    for coordinates in Ecosystem_claim:
        pg.click(coordinates)
        delay(0.4, 0.8)
    Close_AnyWay()
