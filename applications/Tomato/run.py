import time

from applications import *
from applications.Tomato import *
from modules.moves import Close_AnyWay

def Run_Tomato(dailik):
    PreRun(find_Tomato)
    for _ in range(4):
        pg.click(Tomato_claim_and_farm)
        delay()
    pg.click(play_Tomato)
    delay(2, 3)
    for i in range(7):
        time_start = time.time()
        while time.time() - time_start <= 22:
            find_it_and_click_it(Red_Tomato)
            delay(0.01, 0.04)
        delay(10, 20)
        pg.click(start_Tomato_game_again)
    Close_AnyWay()
