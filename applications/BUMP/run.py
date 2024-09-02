from applications import *
from applications.BUMP import *
from modules.moves import Close_AnyWay, swipe_left
from modules.screens import click_on_images


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


def Run_BUMP(dailik, event, win_main):
    find_BUMP = find_BUMP_2 if win_main else find_BUMP_1

    PreRun(find_BUMP, win_main, chat=True, chat_type="click", chatbot_string=1)

    claim_daily_and_swipe_news()

    if event:
        buy_bust_bump()

    for _ in range(16):
        pg.click(middle_screen)
        delay(0.01, 0.1)

    Close_AnyWay()


def claim_daily_and_swipe_news(opposite_direction_numeric=0):
    i_range = [1, 1, 1, 1, 1, 1, 1]
    for i in i_range:
        for _ in range(i):
            drag_to_bottom(duration=0.4, cords_to_drag=cords_to_drag__for_BUMP)
            opposite_direction_numeric = opposite_direction_numeric + 1
        if click_on_images(target_colors=colors_daily):
            break
    for _ in range(opposite_direction_numeric):
        drag_to_up(duration=0.4, cords_to_drag=cords_to_drag__for_BUMP)
    for _ in range(3):
        find_it_and_click_it(green_X)
        find_it_and_click_it(gray_X)
        delay(0.2, 0.4)
    for _ in range(4):
        swipe_left(duration=0.4)
    delay(3, 4)
