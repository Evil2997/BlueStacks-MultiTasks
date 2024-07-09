import pyautogui as pg
from ahk import AHK

from modules.time import delay
from modules.screens import find_it_and_click_it, find_template_on_region, get_image_size

ahk = AHK()


def activate_main_window():
    full_screen = "full_screen"
    for win in ahk.list_windows():
        print(win.title)
        if (
                win.title.startswith("BlueStacks") and
                not win.title.startswith("BlueStacks Multi Instance Manager") and
                not win.title.startswith("BlueStacks-MultiTasks")
        ):
            win.activate()
            find_it_and_click_it(full_screen)
    delay()


def main_cycle(NAMES, special_name_number=-1, special_name=False, width_multiplication=1, width_division=2,
               height_multiplication=1, height_division=2, Delay=False, delay_numeric=-1):
    for name in NAMES:
        if Delay and name == NAMES[delay_numeric]:
            delay(10, 12)
        if special_name and name == NAMES[special_name_number]:
            top_left = find_template_on_region(name)
            width, height = get_image_size(name)
            if top_left:
                pg.click(top_left[0] + width * width_multiplication / width_division,
                         top_left[1] + height * height_multiplication / height_division)
        else:
            result = find_it_and_click_it(name)
            if len(NAMES) == 1:
                return result
        delay()


def open_vpn_telegram(win, win_numeric):
    i = win_numeric
    WIN_START = {
        "win0": {"cords": (540, 200)},
        "win1": {"cords": (540, 250)},
        "win2": {"cords": (540, 310)},
        "win3": {"cords": (540, 360)},
        "win4": {"cords": (540, 420)},
    }

    connect_to_vpn = ["collapse_all_windows", "check_all_windows",
                      "clear_all", "ProtonVPN", "ActivateVPN",
                      "collapse_all_windows"]

    open_telegram = ["collapse_all_windows", "Telegram", "main_group"]

    for _ in range(16):
        win.activate()
        win.move(0, 0)
        delay(0.01, 0.04)
    pg.click(WIN_START[f"win{i}"]["cords"])
    delay(25, 30)
    activate_main_window()
    main_cycle(connect_to_vpn, Delay=True, delay_numeric=4)
    main_cycle(open_telegram)
