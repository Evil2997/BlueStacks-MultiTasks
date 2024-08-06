from applications import *
from applications.BUMP import *
from modules.moves import Close_AnyWay, swipe_left


def buy_bust_bump():
    delay()
    pg.click(open_bust)
    delay()
    drag_to_bottom()
    for coordinates in bust_activate:
        delay()
        pg.click(coordinates)
    pg.press("Esc")
    delay()


def moon_bump():
    pg.press("num4")
    for _ in range(256):
        is_it_clicked = find_it_and_click_it(click_at_moon)
        if is_it_clicked:
            pg.press("num4")
            break
        else:
            delay(0.01, 0.2)
    else:
        pg.press("num4")


def Run_BUMP(dailik):
    PreRun(find_BUMP, chat=True, chat_type="click", chatbot_string=0)
    scan_BUMP_daily_reward()
    delay(2, 3)
    for _ in range(3):
        find_it_and_click_it(green_X)
        find_it_and_click_it(gray_X)
        delay(0.4, 0.6)
        for _ in range(2):
            swipe_left()
            delay(0.4, 0.6)
    # buy_bust_bump()
    for _ in range(16):
        pg.click(middle_screen)
        delay(0.01, 0.1)
    # moon_bump()
    Close_AnyWay()
