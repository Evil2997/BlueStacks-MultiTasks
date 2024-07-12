def WINDOWS_PARAMS():
    # [windows_params]-[START]
    A, B, Q, R, Z = 871, 872, 509, 510, 0
    WIN_POSITION = {
        "win0": {"Win_Name": "BlueStacks 0",
                 "X": Z, "Y": Z, "WIDTH": A, "HEIGHT": Q,
                 "region": (Z, Z, A, Q)},
        "win1": {"Win_Name": "BlueStacks 1",
                 "X": B, "Y": Z, "WIDTH": A, "HEIGHT": Q,
                 "region": (B, Z, B + A, Q)},
        "win2": {"Win_Name": "BlueStacks 2",
                 "X": Z, "Y": R, "WIDTH": A, "HEIGHT": Q,
                 "region": (Z, R, A, Q + R)},
        "win3": {"Win_Name": "BlueStacks 3",
                 "X": B, "Y": R, "WIDTH": A, "HEIGHT": Q,
                 "region": (B, R, B + A, Q + R)},
    }
    # [windows_params]-[END]


import json
from datetime import datetime, timezone, timedelta


class RewardTracker:
    def __init__(self, json_file):
        self.json_file = json_file
        self.load_rewards()

    def load_rewards(self):
        with open(self.json_file, 'r') as file:
            self.app_rewards = json.load(file)

    def save_rewards(self):
        with open(self.json_file, 'w') as file:
            json.dump(self.app_rewards, file, indent=4)

    def check_reward(self, window_id, app_name):
        current_time_utc = datetime.now(timezone.utc)
        formatted_current_time = current_time_utc.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Текущее время UTC: {formatted_current_time}")

        reward_key = f"daily_reward_{app_name}"

        default_time = datetime(2002, 10, 29, 10, 0, 0, tzinfo=timezone.utc)
        default_time_str = default_time.strftime("%Y-%m-%d %H:%M:%S")

        if window_id not in self.app_rewards:
            self.app_rewards[window_id] = {}

        if reward_key not in self.app_rewards[window_id]:
            self.app_rewards[window_id][reward_key] = default_time_str

        last_reward_time_str = self.app_rewards[window_id][reward_key]

        try:
            last_reward_time = datetime.strptime(last_reward_time_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
        except ValueError:
            last_reward_time = default_time
            self.app_rewards[window_id][reward_key] = default_time_str

        next_reward_time = last_reward_time.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)

        if current_time_utc >= next_reward_time:
            return True, next_reward_time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return False, next_reward_time.strftime("%Y-%m-%d %H:%M:%S")

    def update_time_reward(self, window_id, app_name, reward_key):
        current_time_utc = datetime.now(timezone.utc)
        formatted_current_time = current_time_utc.strftime("%Y-%m-%d %H:%M:%S")

        self.app_rewards[window_id][reward_key] = formatted_current_time
        self.save_rewards()


reward_tracker = RewardTracker('Rewards.json')

# Пример использования для двух окон и нескольких приложений
windows = ["win0"]#, "win1"]
apps = ["Blum"]
        # , "Diamond", "Clayton", "BUMP", "PocketFi", "HEXN", "DejenDog", "Seeds", "SimpleCoin", "ElonMusk", "BEE",
        # "TimeFarm"]

for window in windows:
    for app in apps:
        received_today, next_reward_time = reward_tracker.check_reward(window, app)
        print(received_today, next_reward_time)
        if received_today:
            print(f"Награда для {app} в окне {window} может быть получена сегодня.")
        else:
            print(f"Награда для {app} в окне {window} уже получена сегодня.")
        print(f"Следующая ближайшая награда для {app} в окне {window}: {next_reward_time}")
