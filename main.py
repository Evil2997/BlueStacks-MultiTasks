import pathlib
import time
from typing import Final

from ahk import AHK

from applications.BEE.run import Run_BEE
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

from modules.Timers import check_reward as CHECK_DAILY_REWARD
from modules.Timers import delay
from modules.Timers import timer_checker as TIME_CHECK
from modules.Timers import timer_update as UPDATE_TIMER
from modules.Timers import update_time_reward as UPDATE_TIME_DAILY_REWARD
from modules.json_files import load_data
from modules.json_files import align_json_values as SORTED_JSON
from modules.windows import Stop_BS_Windows
from modules.windows import activate_window as ACTIVATE_WINDOW

ahk = AHK()


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
    window_numbers = len(Settings)

    rewards_file = "Rewards.json"
    path_to_Rewards: Final[pathlib.Path] = pathlib.Path(__file__).parent / rewards_file
    Rewards = load_data(path_to_Rewards)

    Game_Details = {
        # "Blum": {"seconds": 28800, "function": Run_Blum},
        # "Diamond": {"seconds": 28800, "function": Run_Diamond},
        # "Clayton": {"seconds": 28800, "function": Run_Clayton},
        # "BUMP": {"seconds": 21600, "function": Run_BUMP},
        # "PocketFi": {"seconds": 18000, "function": Run_PocketFi},
        # "HEXN": {"seconds": 14400, "function": Run_HEXN},
        # "Seeds": {"seconds": 14400, "function": Run_Seeds},
        # "SimpleCoin": {"seconds": 28800, "function": Run_SimpleCoin},
        # "ElonMusk": {"seconds": 10800, "function": Run_ElonMusk},
        # "BEE": {"seconds": 10800, "function": Run_BEE},
        # "TimeFarm": {"seconds": 14400, "function": Run_TimeFarm},
        # "Baboon": {"seconds": 43200, "function": Run_Baboon},
        # "Time_TON_Ecosystem": {"seconds": 28800, "function": Run_Time_TON_Ecosystem},
        # "TON_Station": {"seconds": 28800, "function": Run_TON_Station},
        # "Cyber_Finance": {"seconds": 7200, "function": Run_Cyber_Finance},  # 86400
        # "SnapSter": {"seconds": 86400, "function": Run_SnapSter},
        # "Tomato": {"seconds": Раз в сутки, "function": Run_Tomato},
        # "DejenDog": {"seconds": 14400, "function": Run_DejenDog},
        # +3 game
    }

    # [RUN_SCRIPT]---[START]
    main()
    # [RUN_SCRIPT]---[END]

    print("Время окончания сеанса:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
