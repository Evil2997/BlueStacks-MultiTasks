from applications import *
from applications.Cyber_Finance import *
from modules.moves import Close_AnyWay
from modules.screens import hunt_for_the_button_in_list


def Run_Cyber_Finance(dailik):
    PreRun(find_Cyber_Finance, chat=True, chat_type="click", chatbot_string=2)
    for _ in range(3):
        pg.click(claim_Cyber_Finance)
        delay(0.4, 0.8)
    if dailik:
        pg.click(open_tasks)
        delay()
        for _ in range(20):
            pg.click(daily_video_for_money)
            delay(18, 20)
            pg.click(daily_video_for_money)
            delay()
        pg.press("Esc")
        delay()
    pg.click(open_grades)
    delay()
    for _ in range(grades_numeric):
        for coordinates in upgrade_egg_hummer:
            pg.click(coordinates)
            delay()
    Close_AnyWay()
