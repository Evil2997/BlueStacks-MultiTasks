import pyautogui as pg
from ahk import AHK

from modules.screens import cycle_hunter_click, hunt_for_the_button_in_list
from modules.Timers import delay

ahk = AHK()


def Stop_BS_Windows():
    close_all_windows = ["stop_all_BS_win", "yes_close_all"]
    close_all_BS_window = [(350, 590), (500, 360)]
    for win in ahk.list_windows():
        if win.title.startswith("BlueStacks Multi Instance Manager"):
            for _ in range(8):
                win.activate()
                delay(0.02, 0.2)
            for coordinates in close_all_BS_window:
                pg.click(coordinates)
                delay()


def activate_main_window():
    full_screen = ["full_screen"]
    for win in ahk.list_windows():
        if (
                win.title.startswith("BlueStacks") and
                not win.title.startswith("BlueStacks Multi Instance Manager") and
                not win.title.startswith("BlueStacks-MultiTasks")
        ):
            win.activate()
            hunt_for_the_button_in_list(full_screen, hunt_in_seconds=30)
            break
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

    connect_to_vpn_AND_open_telegram = ["collapse_all_windows", "check_all_windows",
                                        "clear_all", "ProtonVPN", "ActivateVPN",
                                        "collapse_all_windows", "Telegram"]
    main_group = ["main_group"]
    for _ in range(16):
        win.activate()
        win.move(0, 0)
        delay(0.01, 0.04)
    pg.click(WIN_START[f"win{i}"]["cords"])
    delay(25, 30)
    activate_main_window()
    cycle_hunter_click(connect_to_vpn_AND_open_telegram)
    delay(15, 20)
    cycle_hunter_click(main_group)
    delay(8, 10)
