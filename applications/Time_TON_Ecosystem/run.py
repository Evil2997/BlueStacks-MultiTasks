from applications import *
from applications.Time_TON_Ecosystem import *
from modules.moves import Close_AnyWay


def Run_Time_TON_Ecosystem(dailik, event, win_main):
    find_Time_TON_Ecosystem = find_Time_TON_Ecosystem_2 if win_main else find_Time_TON_Ecosystem_1

    PreRun(find_Time_TON_Ecosystem, chat=True, chat_type="click", chatbot_string=2)
    if dailik:
        pg.click(daily_TON_Ecosystem)
        delay()
    pg.click(home_page)
    delay()
    for _ in range(2):
        drag_to_bottom(duration=0.4, cords_to_drag=(940, 300))
    delay()
    for coordinates in Ecosystem_claim:
        pg.click(coordinates)
        delay(0.4, 0.8)
    Close_AnyWay()
