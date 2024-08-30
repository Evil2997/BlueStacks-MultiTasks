from applications import *
from applications.Cyber_Finance import *
from modules.moves import Close_AnyWay
from modules.screens import hunt_for_the_button_in_list


def Run_Cyber_Finance(dailik, event, win_main):
    find_Cyber_Finance = find_Cyber_Finance_2 if win_main else find_Cyber_Finance_1

    PreRun(find_Cyber_Finance, win_main, chat=True, chat_type="click", chatbot_string=2)

    for _ in range(3):
        pg.click(claim_Cyber_Finance)
        delay(0.4, 0.8)
    if dailik:
        pg.click(open_tasks)
        delay()
        find_it_and_click_it(CyberFinance_play_video_ads)
        delay(16, 18)
        for _ in range(32):
            if find_it_and_click_it(CyberFinance_play_next_video):
                delay(16, 18)
        pg.press("Esc")
        delay()
    pg.click(open_grades)
    delay()
    for _ in range(grades_numeric):
        for coordinates in upgrade_egg_hummer:
            pg.click(coordinates)
            delay()
    Close_AnyWay()
