from applications import *
from applications.SimpleCoin import *
from modules.moves import Close_AnyWay


def Run_SimpleCoin(dailik, event, win_main):
    find_SimpleCoin = find_SimpleCoin_2 if win_main else find_SimpleCoin_1
    num_clicker = 16 if win_main else 2

    PreRun(find_SimpleCoin, win_main)

    pg.click(news_click)
    delay()
    for _ in range(4):
        pg.click(claim_SimpleCoins)
        delay()

    # fortuna_ring()

    for _ in range(num_clicker):
        auto_taps()
        delay(0.2, 0.3)

    Close_AnyWay()


def fortuna_ring():
    pg.click(fortuna_open)
    delay()
    pg.click(fortuna_run)
    delay(4, 5)
    find_it_and_click_it(fortuna_reward)
    find_it_and_click_it(fortuna_null_reward)
    delay()


def auto_taps():
    pg.press("num2")
    delay(8, 9)
    pg.press("num2")
