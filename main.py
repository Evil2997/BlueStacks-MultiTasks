import logging
import pathlib
import time
from typing import Final

from ahk import AHK

from applications.BEE.run import Run_BEE
from applications.BOOMS.run import Run_BOOMS
from applications.BUMP.run import Run_BUMP
from applications.Baboon.run import Run_Baboon
from applications.Blum.run import Run_Blum
from applications.Clayton.run import Run_Clayton
from applications.Cyber_Finance.run import Run_Cyber_Finance
from applications.DejenDog.run import Run_DejenDog
from applications.Diamond.run import Run_Diamond
from applications.ElonMusk.run import Run_ElonMusk
from applications.HEXN.run import Run_HEXN
from applications.PocketFi.run import Run_PocketFi
from applications.Seeds.run import Run_Seeds
from applications.SimpleCoin.run import Run_SimpleCoin
from applications.SnapSter.run import Run_SnapSter
from applications.TON_Station.run import Run_TON_Station
from applications.TimeFarm.run import Run_TimeFarm
from applications.Time_TON_Ecosystem.run import Run_Time_TON_Ecosystem
from applications.Tomato.run import Run_Tomato

from modules.Timers import check_reward as CHECK_DAILY_REWARD, time_end_print
from modules.Timers import timer_checker as TIME_CHECK
from modules.Timers import timer_buster as TIME_TO_EXTRA_BONUS
from modules.Timers import timer_update as UPDATE_TIMER
from modules.Timers import timer_update_buster as UPDATE_TIME_TO_EXTRA_BONUS
from modules.Timers import update_time_reward as UPDATE_TIME_DAILY_REWARD
from modules.json_files import load_data
from modules.json_files import align_json_values as SORTED_JSON
from modules.tesseract import setup_tesseract
from modules.windows import Stop_BS_Windows
from modules.windows import activate_window as ACTIVATE_WINDOW

ahk = AHK()


def main():
    while True:
        ACTIVATE = False
        for win in ahk.list_windows():
            if win.title.startswith("BlueStacks Multi Instance Manager"):
                for i in range(window_numbers):
                    games_is_activated_now = []
                    for game, value in Game_Settings.items():
                        sec = value["seconds"]
                        if TIME_CHECK(seconds=sec, window_number=i, game=game, settings_file=settings_file):
                            ACTIVATE = True
                            games_is_activated_now.append(game)
                    if ACTIVATE:
                        ACTIVATE_WINDOW(win, i)
                        print(
                            f"Текущее время: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}, Номер окна: {i}, Запущено было:{games_is_activated_now}")
                        for game, value in Game_Settings.items():
                            sec = value["seconds"]
                            if value["special_event_1"]:
                                sec_1 = value["special_event_1"]
                            else:
                                sec_1 = False
                            if TIME_CHECK(seconds=sec, window_number=i, game=game, settings_file=settings_file):
                                if CHECK_DAILY_REWARD(window_number=i, game=game, rewards_file=rewards_file):
                                    get_daily_rewards_in_this_game = True
                                else:
                                    get_daily_rewards_in_this_game = False
                                if TIME_TO_EXTRA_BONUS(seconds=sec_1, window_number=i, game=game,
                                                       special_events__file=special_events__file):
                                    extra_bonus__special_event = True
                                else:
                                    extra_bonus__special_event = False
                                Game_Settings[game]["function"](
                                    get_daily_rewards_in_this_game, extra_bonus__special_event)
                                UPDATE_TIMER(window_numeric=i, game=game, settings_file=settings_file)
                                SORTED_JSON(settings_file, settings_file)
                                if CHECK_DAILY_REWARD(window_number=i, game=game, rewards_file=rewards_file):
                                    UPDATE_TIME_DAILY_REWARD(window_numeric=i, game=game, rewards_file=rewards_file)
                                    SORTED_JSON(rewards_file, rewards_file)
                                if TIME_TO_EXTRA_BONUS(seconds=sec, window_number=i, game=game,
                                                       special_events__file=special_events__file):
                                    UPDATE_TIME_TO_EXTRA_BONUS(window_numeric=i, game=game,
                                                               special_events__file=special_events__file)
                                    SORTED_JSON(special_events__file, special_events__file)

                        Stop_BS_Windows()
                        ACTIVATE = False
                time.sleep(600)
                break
    pass


if __name__ == '__main__':
    setup_tesseract()

    MAIN_DIR: Final[pathlib.Path] = pathlib.Path(__file__).parent

    settings_file = "Settings.json"
    path_to_Settings: Final[pathlib.Path] = MAIN_DIR / settings_file
    Settings = load_data(path_to_Settings)

    window_numbers = len(Settings)

    rewards_file = "Rewards.json"
    path_to_Rewards: Final[pathlib.Path] = MAIN_DIR / rewards_file
    Rewards = load_data(path_to_Rewards)

    special_events__file = "Special_Events.json"
    path_to__Special_Events: Final[pathlib.Path] = MAIN_DIR / special_events__file
    Special_Events = load_data(path_to__Special_Events)


    Game_Settings = {
        "Blum": {"seconds": 8 * 3600, "function": Run_Blum},
        "Diamond": {"seconds": 8 * 3600, "function": Run_Diamond},
        "Clayton": {"seconds": 8 * 3600, "function": Run_Clayton},
        "BUMP": {"seconds": 6 * 3600, "function": Run_BUMP,
                 "special_event_1": 30 * 24 * 3600},
        "BEE": {"seconds": 2 * 3600, "function": Run_BEE},
        "SimpleCoin": {"seconds": 8 * 3600, "function": Run_SimpleCoin},
        "HEXN": {"seconds": 4 * 3600, "function": Run_HEXN},
        "TimeFarm": {"seconds": 4 * 3600, "function": Run_TimeFarm},
        "Baboon": {"seconds": 12 * 3600, "function": Run_Baboon},
        "Time_TON_Ecosystem": {"seconds": 8 * 3600, "function": Run_Time_TON_Ecosystem},
        "TON_Station": {"seconds": 8 * 3600, "function": Run_TON_Station},
        "Cyber_Finance": {"seconds": 24 * 3600, "function": Run_Cyber_Finance},  # 86400
        "SnapSter": {"seconds": 12 * 3600, "function": Run_SnapSter},
        # "Tomato": {"seconds": 23*3600, "function": Run_Tomato},
        # "ElonMusk": {"seconds": 3*3600, "function": Run_ElonMusk},
        # "PocketFi": {"seconds": 5 * 3600, "function": Run_PocketFi},
        # "Seeds": {"seconds": 4 * 3600, "function": Run_Seeds},
        # "DejenDog": {"seconds": 4*3600, "function": Run_DejenDog},
        # +3 game
    }

    # [RUN_SCRIPT]---[START]
    time_start = time.time()
    try:
        # Run_BOOMS(True, False)
        main()
    except KeyboardInterrupt:
        pass
    # [RUN_SCRIPT]---[END]
    print(f"Время окончания сеанса: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
    time_end = time.time()
    time_end_print(time_end, time_start)
