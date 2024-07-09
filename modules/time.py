import pathlib
import random
import time
from datetime import datetime, timedelta
from typing import Final

from modules.json import save_data, load_data


def delay(min_seconds: float = 1.0, max_seconds: float = 2.0):
    time.sleep(random.uniform(min_seconds, max_seconds))


def timer_checker(seconds, window_number, game, settings_file):
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
    else:
        return False


def timer_update(settings_file, window_numeric, game):
    i = window_numeric
    path_to_Settings: Final[pathlib.Path] = pathlib.Path(__file__).parent.parent / settings_file
    Settings = load_data(path_to_Settings)

    Settings[f"win{i}"][f"time_start_{game}"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_data(path_to_Settings, Settings)
