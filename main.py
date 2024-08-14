import pathlib
import time
from typing import Final

import pyautogui as pg
from ahk import AHK

from applications import PreRun
from applications.BEE.run import Run_BEE
from applications.BUMP.run import Run_BUMP
from applications.Blum.run import Run_Blum
from applications.Clayton.run import Run_Clayton
from applications.Diamond.run import Run_Diamond
from applications.ElonMusk.run import Run_ElonMusk
from applications.HEXN.run import Run_HEXN
from applications.PocketFi.run import Run_PocketFi
from applications.Seeds.run import Run_Seeds
from applications.SimpleCoin.run import Run_SimpleCoin
from applications.TimeFarm.run import Run_TimeFarm
from modules.Timers import check_reward as CHECK_DAILY_REWARD
from modules.Timers import delay
from modules.Timers import timer_checker as TIME_CHECK
from modules.Timers import timer_update as UPDATE_TIMER
from modules.Timers import update_time_reward as UPDATE_TIME_DAILY_REWARD
from modules.json_files import load_data
from modules.json_files import align_json_values as SORTED_JSON
from modules.moves import Close_AnyWay, drag_to_bottom
from modules.screens import find_it_and_click_it, hunt_for_the_button_in_list
from modules.windows import Stop_BS_Windows
from modules.windows import activate_window as ACTIVATE_WINDOW

ahk = AHK()
# pyautogui.FailSafeException: PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen.
# To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED.

def Run_DejenDog(dailik):
    PreRun(find_DejenDog, chat=True, chat_type="image", chat_image_name=ChatDog)
    drag_to_bottom(duration=0.4)
    for _ in range(3):
        pg.press("num3")  # ON
        delay(16, 24)
        pg.press("num3")  # OFF
        delay(4, 6)
    for coordinates in dog_lvlup_menu:
        pg.click(coordinates)
        delay(8, 9)
    Close_AnyWay()


def Run_Baboon(dailik):
    PreRun(find_Baboon, chat=True, chat_type="click", chatbot_string=0)
    if dailik:
        for coordinates in Baboon_daily_reward:
            pg.click(coordinates)
            delay(0.4, 0.8)
        for battery in combo_battery:
            pg.click(battery)
            delay(0.4, 0.8)
        pg.press("Esc")
        delay()
    for _ in range(4):
        pg.press("num3")
        delay(20, 25)
        pg.press("num3")
        delay()
    for coordinates in repair_battery:
        pg.click(coordinates)
        delay()
    Close_AnyWay()


def Run_Tomato(dailik):
    PreRun(find_Tomato)
    for _ in range(4):
        pg.click(Tomato_claim_and_farm)
        delay()
    pg.click(play_Tomato)
    delay(2, 3)
    for i in range(7):
        time_start = time.time()
        while time.time() - time_start <= 22:
            find_it_and_click_it(Red_Tomato)
            delay(0.01, 0.04)
        delay(10, 20)
        pg.click(start_Tomato_game_again)
    Close_AnyWay()


def Run_Time_TON_Ecosystem(dailik):
    PreRun(find_Time_TON_Ecosystem, chat=True, chat_type="click", chatbot_string=2)
    if dailik:
        pg.click(daily_TON_Ecosystem)
    drag_to_bottom(duration=0.4)
    for coordinates in Ecosystem_claim:
        pg.click(coordinates)
        delay(0.4, 0.8)
    Close_AnyWay()


def Run_TON_Station(dailik):
    PreRun(find_TON_Station)
    for _ in range(2):
        pg.click(TON_Station_claim)
        delay(3, 4)
    Close_AnyWay()


def Run_Cyber_Finance(dailik):
    PreRun(find_Cyber_Finance, chat=True, chat_type="click", chatbot_string=2)
    pg.click(claim_Cyber_Finance)
    delay(0.4, 0.8)
    for coordinates in upgrade_egg_hummer:
        pg.click(coordinates)
        delay(0.4, 0.6)
    hunt_for_the_button_in_list(hummer_close)
    Close_AnyWay()


def Run_SnapSter(dailik):
    PreRun(find_SnapSter, chat=True, chat_type="click", chatbot_string=1)
    pg.click(SnapSter_claim_and_farm)
    delay(0.4, 0.6)
    Close_AnyWay()


def main():
    while True:
        ACTIVATE = False
        for win in ahk.list_windows():
            if win.title.startswith("BlueStacks Multi Instance Manager"):
                for i in range(window_numbers):
                    for game, value in Game_Details.items():
                        sec = value["seconds"]
                        if TIME_CHECK(seconds=sec, window_number=i, game=game, settings_file=settings_file):
                            ACTIVATE = True
                    if ACTIVATE:
                        ACTIVATE_WINDOW(win, i)
                        print("Текущее время:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                        for game, value in Game_Details.items():
                            sec = value["seconds"]
                            if TIME_CHECK(seconds=sec, window_number=i, game=game, settings_file=settings_file):
                                if CHECK_DAILY_REWARD(window_number=i, game=game, rewards_file=rewards_file):
                                    get_daily_rewards_in_this_game = True
                                else:
                                    get_daily_rewards_in_this_game = False
                                Game_Details[game]["function"](get_daily_rewards_in_this_game)
                                UPDATE_TIMER(window_numeric=i, game=game, settings_file=settings_file)
                                SORTED_JSON(settings_file, settings_file)
                                if CHECK_DAILY_REWARD(window_number=i, game=game, rewards_file=rewards_file):
                                    UPDATE_TIME_DAILY_REWARD(window_numeric=i, game=game, rewards_file=rewards_file)
                                    SORTED_JSON(rewards_file, rewards_file)
                        Stop_BS_Windows()
                        ACTIVATE = False
                time.sleep(600)
                break
    pass


if __name__ == '__main__':
    settings_file = "Settings.json"
    path_to_Settings: Final[pathlib.Path] = pathlib.Path(__file__).parent / settings_file
    Settings = load_data(path_to_Settings)

    rewards_file = "Rewards.json"
    path_to_Rewards: Final[pathlib.Path] = pathlib.Path(__file__).parent / rewards_file
    Rewards = load_data(path_to_Rewards)

    Game_Details = {
        "Blum": {"seconds": 28800, "function": Run_Blum},
        "Diamond": {"seconds": 28800, "function": Run_Diamond},
        "Clayton": {"seconds": 28800, "function": Run_Clayton},
        # "BUMP": {"seconds": 21600, "function": Run_BUMP},
        "PocketFi": {"seconds": 18000, "function": Run_PocketFi},
        "HEXN": {"seconds": 14400, "function": Run_HEXN},
        "Seeds": {"seconds": 14400, "function": Run_Seeds},
        "SimpleCoin": {"seconds": 28800, "function": Run_SimpleCoin},
        "ElonMusk": {"seconds": 10800, "function": Run_ElonMusk},
        "BEE": {"seconds": 10800, "function": Run_BEE},
        "TimeFarm": {"seconds": 14400, "function": Run_TimeFarm},
        # "Baboon": {"seconds": 43200, "function": Run_Baboon},
        # "Time_TON_Ecosystem": {"seconds": 28800, "function": Run_Time_TON_Ecosystem},
        # "TON_Station": {"seconds": 28800, "function": Run_TON_Station},
        # "Cyber_Finance": {"seconds": 7200, "function": Run_Cyber_Finance},  # 86400
        # "SnapSter": {"seconds": 86400, "function": Run_SnapSter},
        # "Tomato": {"seconds": Раз в сутки, "function": Run_Tomato},
        # "DejenDog": {"seconds": 14400, "function": Run_DejenDog},
        # +3 game
    }

    if True:
        number_bottom_drags = len(Game_Details) * 4
        window_numbers = len(Settings)
        # [names_for_images]---[START]
        connect_to_vpn = ["collapse_all_windows", "check_all_windows",
                          "clear_all", "ProtonVPN", "ActivateVPN",
                          "collapse_all_windows"]
        main_group = ["main_group"]
        cords_close = (116, 132)
        click_to_bottom_in_BotChat = [(890, 880), (890, 800), (890, 720)]
        middle_screen = (960, 540)
        close_main_group = (730, 130)
        bug_while_scrolling_chat = "bug_while_scrolling_chat"
        # [names_for_images]---[END]

        find_DejenDog = ["DejenDog"]
        ChatDog = ["ChatDog_Enter"]
        dog_lvlup_menu = [(940, 950), (800, 440)]

        find_Baboon = ["Baboon"]
        Baboon_daily_reward = [(950, 950), (690, 890), (940, 1000)]
        combo_battery = [(740, 420), (940, 420), (1140, 420), (950, 950)]
        bust_battery = [(1060, 900), (1000, 660), (930, 980)]
        repair_battery = [(1200, 770), (930, 980)]

        find_Time_TON_Ecosystem = ["Time_TON_Ecosystem"]
        daily_TON_Ecosystem = (950, 920)
        Ecosystem_claim = [(940, 890), (1045, 965), (940, 500)]

        find_TON_Station = ["TON_Station"]
        TON_Station_claim = (950, 800)

        find_Cyber_Finance = ["Cyber_Finance"]
        hummer_close = ["hummer_close"]
        claim_Cyber_Finance = (940, 540)
        upgrade_egg_hummer = [(1470, 860), (1470, 860), (1060, 740)]

        find_SnapSter = ["SnapSter"]
        SnapSter_claim_and_farm = (1350, 540)

    # To Do: Set cords / make images
    find_Tomato = ["Tomato"]
    Red_Tomato = ["Red_Tomato"]
    Tomato_claim_and_farm = ()
    play_Tomato = ()
    start_Tomato_game_again = ()

    # [RUN_SCRIPT]---[START]
    main()
    # [RUN_SCRIPT]---[END]

    print("Время окончания сеанса:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
