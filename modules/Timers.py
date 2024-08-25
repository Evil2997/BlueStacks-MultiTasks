import pathlib
import random
import time
from datetime import datetime, timedelta, timezone
from typing import Final

from modules import MAIN_DIR
from modules.json_files import save_data, load_data


def time_end_print(time_end, time_start):
    elapsed_time = time_end - time_start
    days = elapsed_time // (24 * 3600)
    hours = (elapsed_time % (24 * 3600)) // 3600
    minutes = (elapsed_time % 3600) // 60
    seconds = elapsed_time % 60
    print(f"Время работы процесса: {int(days)} дней, {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд")



def delay(min_seconds: float = 1.0, max_seconds: float = 2.0):
    time.sleep(random.uniform(min_seconds, max_seconds))


def timer_checker(seconds, window_number, game, settings_file):
    if seconds:
        i = window_number
        path_to_Settings: Final[pathlib.Path] = pathlib.Path(__file__).parent.parent / settings_file
        Settings = load_data(path_to_Settings)

        default_timestamp_HUMAN = "2002-10-29 10:00:00"
        current_time = datetime.now()
        try:
            timestamp = datetime.strptime(Settings[f"win{i}"][f"time_start_{game}"], "%Y-%m-%d %H:%M:%S")
        except (ValueError, KeyError, TypeError):
            Settings[f"win{i}"][f"time_start_{game}"] = default_timestamp_HUMAN
            save_data(path_to_Settings, Settings)
            timestamp = datetime.strptime(default_timestamp_HUMAN, "%Y-%m-%d %H:%M:%S")

        time_difference = current_time - timestamp
        if time_difference >= timedelta(seconds=seconds):
            return True
    return False


def timer_update(settings_file, window_numeric, game):
    i = window_numeric
    path_to_Settings: Final[pathlib.Path] = pathlib.Path(__file__).parent.parent / settings_file
    Settings = load_data(path_to_Settings)

    Settings[f"win{i}"][f"time_start_{game}"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_data(path_to_Settings, Settings)


def check_reward(window_number, game, rewards_file):

    i = window_number
    path_to_Rewards: Final[pathlib.Path] = pathlib.Path(__file__).parent.parent / rewards_file
    Rewards = load_data(path_to_Rewards)

    default_time = datetime(2002, 10, 29, 10, 0, 0, tzinfo=timezone.utc)
    default_time_str = default_time.strftime("%Y-%m-%d %H:%M:%S")

    try:
        last_reward_time = datetime.strptime(Rewards[f"win{i}"][f"daily_reward_{game}"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    except (ValueError, KeyError, TypeError):
        last_reward_time = default_time
        Rewards[f"win{i}"][f"daily_reward_{game}"] = default_time_str
        save_data(path_to_Rewards, Rewards)

    next_reward_time = last_reward_time.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    next_reward_time.strftime("%Y-%m-%d %H:%M:%S")
    current_time_utc = datetime.now(timezone.utc)

    if current_time_utc >= next_reward_time:
        return True
    return False


def update_time_reward(rewards_file, window_numeric, game):
    i = window_numeric
    path_to_Rewards: Final[pathlib.Path] = pathlib.Path(__file__).parent.parent / rewards_file
    Rewards = load_data(path_to_Rewards)

    Rewards[f"win{i}"][f"daily_reward_{game}"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    save_data(file_path=path_to_Rewards, data=Rewards)


def timer_buster(seconds, window_number, game, special_events__file):
    if seconds:
        i = window_number
        path_to__Special_Events: Final[pathlib.Path] = MAIN_DIR / special_events__file
        Special_Events = load_data(path_to__Special_Events)

        default_timestamp_HUMAN = "2002-10-29 10:00:00"
        current_time = datetime.now()

        win_key = f"win{i}"
        time_key = f"time_start_{game}"

        if win_key not in Special_Events:
            Special_Events[win_key] = {}

        if time_key not in Special_Events[win_key]:
            Special_Events[win_key][time_key] = default_timestamp_HUMAN
            save_data(path_to__Special_Events, Special_Events)

        try:
            timestamp = datetime.strptime(Special_Events[win_key][time_key], "%Y-%m-%d %H:%M:%S")
        except (ValueError, KeyError, TypeError):
            Special_Events[win_key][time_key] = default_timestamp_HUMAN
            save_data(path_to__Special_Events, Special_Events)
            timestamp = datetime.strptime(default_timestamp_HUMAN, "%Y-%m-%d %H:%M:%S")

        time_difference = current_time - timestamp
        if time_difference >= timedelta(seconds=seconds):
            return True
    return False


def timer_update_buster(special_events__file, window_numeric, game):
    i = window_numeric

    path_to__Special_Events: Final[pathlib.Path] = MAIN_DIR / special_events__file
    Special_Events = load_data(path_to__Special_Events)

    Special_Events[f"win{i}"][f"time_start_{game}"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_data(path_to__Special_Events, Special_Events)
