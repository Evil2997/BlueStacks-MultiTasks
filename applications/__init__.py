from typing import Literal, List

import pyautogui as pg

from modules import main_group
from modules.Timers import delay
from modules.moves import drag_to_up, drag_to_bottom
from modules.screens import find_it_and_click_it, cycle_hunter_click, find_template_in_region, \
    hunt_for_the_button_in_list

connect_to_vpn = ["collapse_all_windows", "check_all_windows",
                  "clear_all", "ProtonVPN", "ActivateVPN",
                  "collapse_all_windows"]
telegram = ["Telegram"]
bug_while_scrolling_chat = "bug_while_scrolling_chat"

cords_to_drag__standard = (1700, 300)
cords_to_drag__win_main = (900, 300)
cords_close = (116, 132)
middle_screen = (960, 540)
close_main_group = (730, 130)
click_to_bottom_in_BotChat = [(900, 880), (900, 800), (900, 720)]


def primary_hunter_click(finder, threshold, win_main=False,
                         initial_setup_clicker=False,
                         initial_setup_images: List[str] = None):
    MAIN_CYCLE = True
    cords_to_drag = cords_to_drag__win_main if win_main else cords_to_drag__standard

    while MAIN_CYCLE:
        if not MAIN_CYCLE:
            break
        hunt_for_the_button_in_list(main_group, hunt_in_seconds=2)
        for _ in range(4):
            delay(0.02, 0.1)
            pg.click(close_main_group)
        delay()
        hunt_for_the_button_in_list(main_group, hunt_in_seconds=2)
        for _ in range(16):
            if not MAIN_CYCLE:
                break
            if find_template_in_region(bug_while_scrolling_chat):
                pg.click(close_main_group)
                hunt_for_the_button_in_list(main_group, hunt_in_seconds=2)
            for _ in range(20):
                if find_it_and_click_it(finder, threshold=threshold):
                    MAIN_CYCLE = False
                    if initial_setup_clicker:
                        find_it_and_click_it(initial_setup_images)
                    break
                else:
                    drag_to_up(cords_to_drag=cords_to_drag)


def PreRun(finder,
           win_main: bool = False,
           chat: bool = False,
           chat_type: Literal["image", "click"] = "click",
           chatbot_string: int = -1,
           chat_image_name: List[str] = None,
           threshold: float = 0.92,
           initial_setup_clicker=False,
           initial_setup_images: List[str] = None
           ):
    if chat_type not in ["image", "click"]:
        raise ValueError("chat_type должен быть 'image' или 'click'")
    # [---Start---]
    for _ in range(8):
        if find_it_and_click_it(main_group):
            find_it_and_click_it(main_group)
            break
        delay(0.04, 0.6)
    drag_to_bottom()

    primary_hunter_click(
        finder=finder, win_main=win_main, threshold=threshold,
        initial_setup_clicker=initial_setup_clicker,
        initial_setup_images=initial_setup_images,
    )

    if chat:
        delay(4, 5)
        if chat_type == "click":
            pg.click(click_to_bottom_in_BotChat[chatbot_string])
        elif chat_type == "image":
            cycle_hunter_click(chat_image_name)
    delay(24, 25)
