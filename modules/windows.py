import pyautogui as pg
from ahk import AHK

from modules import *
from modules.Timers import delay
from modules.screens import cycle_hunter_click, hunt_for_the_button_in_list, find_it_and_click_it

ahk = AHK()


def Stop_BS_Windows():
    for win in ahk.list_windows():
        if win.title.startswith("BlueStacks Multi Instance Manager"):
            for _ in range(8):
                win.activate()
                delay(0.02, 0.2)
            for coordinates in close_all_BS_window:
                pg.click(coordinates)
                delay()


def activate_main_window():
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


def activate_window(win, win_numeric):
    i = win_numeric
    for _ in range(16):
        win.activate()
        win.move(0, 0)
        delay(0.01, 0.04)
    pg.click(WIN_START[f"win{i}"]["cords"])
    delay(30, 40)
    activate_main_window()
    cycle_hunter_click(connect_to_vpn_AND_open_telegram)
    delay()
    find_it_and_click_it(Telegram)
    delay(20, 30)
    hunt_for_the_button_in_list(main_group)
    delay(14, 16)
