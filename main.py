import pathlib
import random
import time
from typing import Final

from ahk import AHK

from applications.BEE.run import Run_BEE
from applications.BOOMS.run import Run_BOOMS
from applications.BUMP.run import Run_BUMP
from applications.Baboon.run import Run_Baboon
from applications.Blum.run import Run_Blum
from applications.Clayton.run import Run_Clayton
from applications.Diamond.run import Run_Diamond
from applications.HEXN.run import Run_HEXN
from applications.SimpleCoin.run import Run_SimpleCoin
from applications.SnapSter.run import Run_SnapSter
from applications.TON_Station.run import Run_TON_Station
from applications.TimeFarm.run import Run_TimeFarm
from modules import window_numbers
from modules.Timers import check_reward as CHECK_DAILY_REWARD, time_end_print
from modules.Timers import timer_buster as TIME_TO_EXTRA_BONUS
from modules.Timers import timer_checker as TIME_CHECK
from modules.Timers import timer_update as UPDATE_TIMER
from modules.Timers import timer_update_buster as UPDATE_TIME_TO_EXTRA_BONUS
from modules.Timers import update_time_reward as UPDATE_TIME_DAILY_REWARD
from modules.json_files import align_json_values as SORTED_JSON
from modules.json_files import load_data
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
                    win_main = (i == 5)
                    for game, value in Game_Settings.items():
                        sec = value["seconds"]
                        if TIME_CHECK(seconds=sec, window_number=i, game=game, settings_file=settings_file):
                            ACTIVATE = True
                    if ACTIVATE:
                        Stop_BS_Windows()
                        ACTIVATE_WINDOW(win, i)
                        games_is_activated_now = []

                        for game, value in Game_Settings.items():
                            sec = value["seconds"]
                            try:
                                sec_1 = value["special_event_1"]
                            except KeyError:
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
                                    dailik=get_daily_rewards_in_this_game,
                                    event=extra_bonus__special_event,
                                    win_main=win_main)
                                games_is_activated_now.append(game)
                                UPDATE_TIMER(
                                    window_numeric=i,
                                    game=game,
                                    settings_file=settings_file
                                )
                                SORTED_JSON(settings_file, settings_file)
                                if CHECK_DAILY_REWARD(
                                        window_number=i,
                                        game=game,
                                        rewards_file=rewards_file
                                ):
                                    UPDATE_TIME_DAILY_REWARD(window_numeric=i, game=game, rewards_file=rewards_file)
                                    SORTED_JSON(rewards_file, rewards_file)
                                if TIME_TO_EXTRA_BONUS(seconds=sec_1, window_number=i, game=game,
                                                       special_events__file=special_events__file):
                                    UPDATE_TIME_TO_EXTRA_BONUS(window_numeric=i, game=game,
                                                               special_events__file=special_events__file)
                                    SORTED_JSON(special_events__file, special_events__file)
                        print(
                            f"Текущее время: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}, Номер окна: {i}, Запущено было:{games_is_activated_now}")

                        Stop_BS_Windows()
                        ACTIVATE = False
                time.sleep(180)
                break
    pass


if __name__ == '__main__':
    setup_tesseract()

    MAIN_DIR: Final[pathlib.Path] = pathlib.Path(__file__).parent

    settings_file = "Settings.json"
    path_to_Settings: Final[pathlib.Path] = MAIN_DIR / settings_file
    Settings = load_data(path_to_Settings)

    rewards_file = "Rewards.json"
    path_to_Rewards: Final[pathlib.Path] = MAIN_DIR / rewards_file
    Rewards = load_data(path_to_Rewards)

    special_events__file = "Special_Events.json"
    path_to__Special_Events: Final[pathlib.Path] = MAIN_DIR / special_events__file
    Special_Events = load_data(path_to__Special_Events)

    SS = Seconds_time_to_Started = random.randint(30, 40)
    dogiators_time = 2 * 3600 - SS

    Game_Settings = {
        "Blum": {"seconds": 8 * 3600 - SS, "function": Run_Blum},
        "Diamond": {"seconds": 8 * 3600 - SS, "function": Run_Diamond},
        "Clayton": {"seconds": 16 * 3600 - SS, "function": Run_Clayton},
        "SimpleCoin": {"seconds": 8 * 3600 - SS, "function": Run_SimpleCoin},
        # "TON_Station": {"seconds": 8 * 3600 - SS, "function": Run_TON_Station},
        # "BUMP": {"seconds": 6 * 3600 - SS, "function": Run_BUMP,
        #          "special_event_1": 30 * 24 * 3600},
        # "SnapSter": {"seconds": 8 * 3600 - SS, "function": Run_SnapSter},
        # "HEXN": {"seconds": 4 * 3600 - SS, "function": Run_HEXN},
        # "TimeFarm": {"seconds": 8 * 3600 - SS, "function": Run_TimeFarm},
        # "Baboon": {"seconds": 4 * 3600 - SS, "function": Run_Baboon},
        # "BOOMS": {"seconds": 4 * 3600 - SS, "function": Run_BOOMS},
        "BEE": {"seconds": 4 * 3600 - SS, "function": Run_BEE},

        # "Dogiators": {"seconds": dogiators_time, "function": Run_Dogiators,
        #               "special_event_1":  dogiators_time * 3},

        # "Cyber_Finance": {"seconds": 24 * 3600 - SS, "function": Run_Cyber_Finance},
        # "ElonMusk": {"seconds": 600, "function": Run_ElonMusk},

        # "Time_TON_Ecosystem": {"seconds": 8 * 3600, "function": Run_Time_TON_Ecosystem},
        # "Tomato": {"seconds": 23 * 3600, "function": Run_Tomato},
        # "PocketFi": {"seconds": 5 * 3600, "function": Run_PocketFi},
        # "Seeds": {"seconds": 4 * 3600, "function": Run_Seeds},
        # "DejenDog": {"seconds": 4 * 3600, "function": Run_DejenDog},
    }

    # [RUN_SCRIPT]---[START]
    time_start = time.time()
    try:
        main()
    except KeyboardInterrupt:
        pass
    print(f"Время окончания сеанса: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
    time_end = time.time()
    time_end_print(time_end, time_start)
    # [RUN_SCRIPT]---[END]

# SimpleCoin просмотр остатков кликов
# Автоматическое выполнение заданий
# Blum игра
