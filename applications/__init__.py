from typing import Literal, List

import pyautogui as pg

from modules.Timers import delay
from modules.moves import drag_to_up, drag_to_bottom
from modules.screens import find_it_and_click_it, cycle_hunter_click, find_template_on_region

number_bottom_drags = 64  # len(Game_Details) * 4

main_group = ["main_group"]
connect_to_vpn = ["collapse_all_windows", "check_all_windows",
                  "clear_all", "ProtonVPN", "ActivateVPN",
                  "collapse_all_windows"]

bug_while_scrolling_chat = "bug_while_scrolling_chat"

cords_close = (116, 132)
middle_screen = (960, 540)
close_main_group = (730, 130)
click_to_bottom_in_BotChat = [(900, 880), (900, 800), (900, 720)]


def primary_hunter_click(finder, threshold):
    MAIN_CYCLE = True
    while MAIN_CYCLE:
        if not MAIN_CYCLE:
            break
        find_it_and_click_it(main_group)
        for _ in range(3):
            delay(0.4, 0.6)
            pg.click(close_main_group)
        delay(4, 5)
        find_it_and_click_it(main_group)
        for _ in range(20):
            if not MAIN_CYCLE:
                break
            if find_template_on_region(bug_while_scrolling_chat):
                pg.click(close_main_group)
                find_it_and_click_it(main_group)
            for _ in range(20):
                if find_it_and_click_it(finder, threshold=threshold):
                    MAIN_CYCLE = False
                    break
                else:
                    drag_to_up()


def PreRun(finder,
           chat: bool = False,
           chat_type: Literal["image", "click"] = "click",
           chatbot_string: int = -1,
           chat_image_name: List[str] = None,
           threshold: float = 0.92
           ):
    if chat_type not in ["image", "click"]:
        raise ValueError("chat_type должен быть 'image' или 'click'")
    # [---Start---]
    for _ in range(16):
        if find_it_and_click_it(main_group):
            find_it_and_click_it(main_group)
            break
        delay(0.04, 0.6)
    drag_to_bottom()

    primary_hunter_click(finder=finder, threshold=threshold)

    if chat:
        delay(8, 10)
        if chat_type == "click":
            pg.click(click_to_bottom_in_BotChat[chatbot_string])
        elif chat_type == "image":
            cycle_hunter_click(chat_image_name)
    delay(18, 20)
