from applications import *
from applications.BUMP import *
from modules.moves import Close_AnyWay, swipe_left
from modules.screens import click_in_center_on_region_by_color


def Run_BUMP(dailik, event, win_main):
    find_BUMP = find_BUMP_2 if win_main else find_BUMP_1

    PreRun(find_BUMP, win_main, chat=True, chat_type="click", chatbot_string=1)

    claim_daily()

    swipe_news()

    if event:
        buy_bust_bump()

    for _ in range(16):
        pg.click(middle_screen)
        delay(0.01, 0.1)

    Close_AnyWay()


def swipe_news():
    for _ in range(4):
        find_it_and_click_it(X)
        delay(0.04, 0.2)
    for _ in range(4):
        swipe_left(duration=0.4)
        delay(0.04, 0.2)
    delay()


def claim_daily():
    if click_in_center_on_region_by_color(
            target_colors=colors_daily,
            pixel_threshold=500,
            tolerance=3
    ):
        drag_to_bottom(duration=0.4, cords_to_drag=cords_to_drag__for_BUMP)
        for coordinates in daily_reward__1:
            pg.click(coordinates)
            delay(0.04, 0.2)

        drag_to_bottom(duration=0.4, cords_to_drag=cords_to_drag__for_BUMP)
        drag_to_bottom(duration=0.4, cords_to_drag=cords_to_drag__for_BUMP)

        for coordinates in daily_reward__2_3:
            pg.click(coordinates)
            delay(0.04, 0.2)

        drag_to_bottom(duration=0.4, cords_to_drag=cords_to_drag__for_BUMP)
        drag_to_bottom(duration=0.4, cords_to_drag=cords_to_drag__for_BUMP)

        for coordinates in daily_reward__2_3:
            pg.click(coordinates)
            delay(0.04, 0.2)

        drag_to_bottom(duration=0.4, cords_to_drag=cords_to_drag__for_BUMP)
        drag_to_bottom(duration=0.4, cords_to_drag=cords_to_drag__for_BUMP)
        drag_to_bottom(duration=0.4, cords_to_drag=cords_to_drag__for_BUMP)

        for coordinates in daily_reward__4:
            pg.click(coordinates)
            delay(0.04, 0.2)

        for _ in range(9):
            drag_to_up(duration=0.4, cords_to_drag=cords_to_drag__for_BUMP)


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
