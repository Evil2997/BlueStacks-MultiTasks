from applications import *
from applications.SimpleCoin import *
from modules.moves import Close_AnyWay


def Run_SimpleCoin(dailik):
    PreRun(find_SimpleCoin)
    pg.click(news_click)
    delay()
    for _ in range(3):
        pg.click(claim_SimpleCoins)
        delay()
    pg.click(fortuna_open)
    delay()
    pg.click(fortuna_run)
    delay(4, 5)
    find_it_and_click_it(fortuna_reward)
    find_it_and_click_it(fortuna_null_reward)
    delay()
    pg.press("num4")
    delay(16, 18)
    pg.press("num4")
    Close_AnyWay()
