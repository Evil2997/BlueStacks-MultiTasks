import pathlib
import time
from datetime import datetime
from typing import Final
from ahk import AHK

import pyautogui as pg

from modules.json import load_data, save_data
from modules.moves import Close_AnyWay, drag_to_bottom, drag_to_up
from modules.screens import find_it_and_click_it, scan_BUMP_daily_reward
from modules.time import timer_checker, delay
from modules.windows import activate_main_window, main_cycle

ahk = AHK()


def PreRun(finder):
    for _ in range(16):
        if find_it_and_click_it(main_group):
            break
        delay(0.04, 0.6)
    for _ in range(number_bottom_drags):
        drag_to_bottom()
    while True:
        if not main_cycle(finder):
            drag_to_up()
        else:
            break


def Run_Blum():
    PreRun(find_Blum)
    delay(14, 16)
    pg.click(claim_reward_daily)
    delay()
    for _ in range(2):
        pg.click(claim_farm)
        delay(2, 3)
    Close_AnyWay()


def Run_Diamond():
    PreRun(find_Diamond)
    delay(8, 9)
    pg.click(click_diamonds)
    delay(0.4, 0.6)
    pg.press("num5")
    delay(9.5, 10.2)
    pg.press("num5")
    delay(0.4, 0.6)
    pg.click(click_diamonds[0], click_diamonds[1] + 80)
    Close_AnyWay()


def Run_Clayton():
    PreRun(find_Clayton)
    delay(6, 7)
    pg.click(claim_daily_reward)
    delay()
    for _ in range(2):
        pg.click(claim_coins)
        delay()
    Close_AnyWay()


def Run_BUMP():
    PreRun(find_BUMP)
    delay(3, 4)
    drag_to_bottom()
    delay()
    pg.click(click_to_bottom_in_BotChat)
    delay(12, 14)
    scan_BUMP_daily_reward()
    delay()
    for _ in range(2):
        find_it_and_click_it(green_X)
        delay(0.2, 0.5)
    for _ in range(16):
        pg.click(middle_screen)
        delay(0.2, 0.6)
    for _ in range(256):
        is_it_clicked = find_it_and_click_it(click_at_moon)
        delay(0.01, 0.04)
        if is_it_clicked:
            break
        else:
            pg.click(middle_screen)
    Close_AnyWay()


def Run_PocketFi():
    PreRun(find_PocketFi)
    delay(6, 7)
    main_cycle(get_daily_FiReward)
    delay()
    pg.click(get_reward_Fi)
    delay()
    pg.click(cords_close)
    delay()
    find_it_and_click_it(claim_switch)
    Close_AnyWay()


def Run_HEXN():
    PreRun(find_HEXN)
    delay(15, 18)
    pg.click(claim_reward_HEXN)
    delay()
    pg.click(start_farm_HEXN)
    Close_AnyWay()


def Run_DejenDog():
    PreRun(find_DejenDog)
    delay()
    find_it_and_click_it(ChatDog_Enter)
    delay(0.4, 0.6)
    find_it_and_click_it(ChatDog_Start)
    delay(6, 7)
    pg.press("num3")
    delay(80, 90)
    pg.press("num3")
    find_it_and_click_it(dog_lvlup_menu)
    delay()
    pg.click(Dog_LevelUp)
    Close_AnyWay()


def Run_Seeds():
    PreRun(find_Seeds)
    delay(12, 14)
    find_it_and_click_it(seeds_claim)
    delay()
    pg.click(caterpillar_claim_on_tree)
    delay()
    find_it_and_click_it(caterpillar_is_not_ready)
    find_it_and_click_it(sell_caterpillar)
    Close_AnyWay()


def Run_SimpleCoin():
    PreRun(find_SimpleCoin)
    delay(14, 16)
    for _ in range(2):
        delay()
        pg.click(claim_coins)
    find_it_and_click_it(fortuna_open)
    delay()
    pg.click(fortuna_run)
    delay(4, 5)
    find_it_and_click_it(fortuna_reward)
    delay(0.06, 0.2)
    Close_AnyWay()
    delay(0.06, 0.2)
    pg.press("num3")
    delay(9, 10)
    pg.press("num3")

    Close_AnyWay()


def Run_BEE():
    PreRun(find_BEE)
    delay(2, 3)
    pg.click(Chat_open_BEE)
    delay(0.2, 0.4)
    find_it_and_click_it(BEE_sure)
    delay(14, 16)
    pg.press("num9")
    delay(7, 8)
    main_cycle(upgrades_BEE)
    delay(0.2, 0.6)
    pg.press("num9")
    delay(7, 8)
    for _ in range(20):
        pg.click(upgrades_BEE_stage_1)
        delay(0.6, 1)
    for _ in range(20):
        pg.click(upgrades_BEE_stage_2)
        delay(0.6, 1)
    for _ in range(2):
        Close_AnyWay()


def Run_ElonMusk():
    PreRun(find_ElonMusk)
    delay(12, 14)
    find_it_and_click_it(Musk_take)
    Close_AnyWay()


def Run_TimeFarm():
    PreRun(find_TimeFarm)
    delay()
    pg.click(ChatBot_and_FarmingTime)
    delay(10, 14)

    for _ in range(2):
        pg.click(ChatBot_and_FarmingTime)
        delay(2, 3)
    Close_AnyWay()


def main():
    while True:
        ACTIVATE = False
        for win in ahk.list_windows():
            if win.title.startswith("BlueStacks Multi Instance Manager"):
                for i in range(window_numbers):
                    for game, value in Game_Details.items():
                        sec = value["seconds"]
                        if timer_checker(seconds=sec, window_number=i, game=game, settings_file=settings_file):
                            ACTIVATE = True
                    if ACTIVATE:
                        # [ACTIVATE_WINDOW]---[START]
                        for _ in range(16):
                            win.activate()
                            win.move(0, 0)
                            delay(0.01, 0.04)
                        pg.click(WIN_START[f"win{i}"]["cords"])
                        delay(25, 30)
                        activate_main_window()
                        main_cycle(connect_to_vpn, Delay=True, delay_numeric=4)
                        main_cycle(open_telegram)
                        # [ACTIVATE_WINDOW]---[END]
                        print("Текущее время:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                        for game, value in Game_Details.items():
                            sec = value["seconds"]
                            if timer_checker(seconds=sec, window_number=i, game=game, settings_file=settings_file):
                                Game_Details[game]["function"]()
                                # ### UPDATE TIMER ###
                                Settings[f"win{i}"][f"time_start_{game}"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                save_data(path_to_Settings, Settings)
                        main_cycle(close_all_windows)
                        ACTIVATE = False
                time.sleep(600)
    pass


if __name__ == '__main__':
    settings_file = "Settings.json"
    path_to_Settings: Final[pathlib.Path] = pathlib.Path(__file__).parent / settings_file
    Settings = load_data(path_to_Settings)

    Game_Details = {
        "Blum": {"seconds": 28800, "function": Run_Blum},
        "Diamond": {"seconds": 28800, "function": Run_Diamond},
        "Clayton": {"seconds": 28800, "function": Run_Clayton},
        "BUMP": {"seconds": 21600, "function": Run_BUMP},
        "PocketFi": {"seconds": 18000, "function": Run_PocketFi},
        "HEXN": {"seconds": 14400, "function": Run_HEXN},
        "DejenDog": {"seconds": 14400, "function": Run_DejenDog},
        "Seeds": {"seconds": 10800, "function": Run_Seeds},
        "SimpleCoin": {"seconds": 28800, "function": Run_SimpleCoin},
        "ElonMusk": {"seconds": 10800, "function": Run_ElonMusk},
        "BEE": {"seconds": 14400, "function": Run_BEE},
        # "TimeFarm": {"seconds": 14400, "function": Run_TimeFarm},
    }

    WIN_START = {
        "win0": {"cords": (540, 200)},
        "win1": {"cords": (540, 250)},
        "win2": {"cords": (540, 310)},
        "win3": {"cords": (540, 360)},
        "win4": {"cords": (540, 420)},
    }

    if True:
        number_bottom_drags = 25
        window_numbers = len(Settings)
        # [names_for_images]-[main]-[START]
        connect_to_vpn = ["collapse_all_windows", "check_all_windows",
                          "clear_all", "ProtonVPN", "ActivateVPN",
                          "collapse_all_windows"]
        # [names_for_images]-[main]-[END]

        # [Telegram_params]-[Start]
        open_telegram = ["collapse_all_windows", "Telegram", "main_group"]
        # cords_to_drag = (1650, 230)
        # cords_to_start_drag = (1650, 830)
        cords_close = (116, 132)
        farm_group = (127, 364)
        main_group = "main_group"
        # close_anyway = "close_anyway"

        click_to_bottom_in_BotChat = (1000, 880)

        close_all_windows = ["close_window", "close_window_yes"]
        # [Telegram_params]-[End]

        # [Blum_params]-[Start]
        find_Blum = ["Blum"]
        claim_farm = (940, 840)
        claim_reward_daily = (750, 960)
        gray_small_X = "gray_small_X"
        # [Blum_params]-[End]

        # [Diamond_params]-[Start]
        find_Diamond = ["Diamond"]
        click_diamonds = (940, 740)
        # [Diamond_params]-[End]

        # [Clayton_params]-[Start]
        find_Clayton = ["Clayton"]
        claim_daily_reward = (940, 840)
        claim_coins = (940, 820)
        # [Clayton_params]-[End]

        # [BUMP_params]-[Start]
        find_BUMP = ["BUMP"]
        button_position = (1660, 880)
        top_position = (1660, 280)
        green_X = "green_X"
        click_at_moon = "click_at_moon"
        middle_screen = (960, 540)
        # [BUMP_params]-[End]

        # [PocketFi_params]-[Start]
        find_PocketFi = ["PocketFi"]
        claim_switch = "Claim_SWITCH"
        get_daily_FiReward = ["FiQuests", "FiPresent"]
        get_reward_Fi = (940, 980)
        # [PocketFi_params]-[End]

        Dog_LevelUp = (800, 500)
        find_HEXN = ["HEXN"]
        find_DejenDog = ["DejenDog"]
        find_Seeds = ["Seeds"]
        find_SimpleCoin = ["SimpleCoin"]
        dog_lvlup_menu = "dog_lvlup_menu"
        seeds_claim = "seeds_claim"
        caterpillar_is_not_ready = "caterpillar_is_not_ready"
        caterpillar_claim_on_tree = (980, 560)
        fortuna_open = "fortuna_open"
        fortuna_run = (900, 900)
        fortuna_reward = "fortuna_reward"
        sell_caterpillar = "sell_caterpillar"
        ChatDog_Enter = "ChatDog_Enter"
        ChatDog_Start = "ChatDog_Start"
        claim_reward_HEXN = (940, 880)
        start_farm_HEXN = (940, 840)
        Chat_open_BEE = (890, 890)
        BEE_sure = "BEE_sure"
        full_screen_BEE = (1300, 500)
        upgrades_BEE = ["upgrades_BEE", "upgrades_BEE_2"]
        bee_lvl_up = "bee_lvl_up"
        upgrades_BEE_stage_1 = (1100, 550)
        upgrades_BEE_stage_2 = (1100, 280)
        Musk_take = "Musk_take"
        find_BEE = ["BEE"]
        find_ElonMusk = ["ElonMusk"]
        find_TimeFarm = ["TimeFarm"]
        ChatBot_and_FarmingTime = (1000, 800)
    # [RUN_SCRIPT]-[START]
    main()
    # [RUN_SCRIPT]-[END]

    print("Время окончания сеанса:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
