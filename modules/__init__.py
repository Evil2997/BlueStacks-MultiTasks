import pathlib
from typing import Final

# [Moves]---[Start]
cords_to_drag = (1700, 300)
cords_close = (116, 132)
cords_to_swipe = (700, 440)
close_anyway = ["close_anyway"]
# [Moves]---[End]

# [Windows]---[Start]
connect_to_vpn_AND_open_telegram = [
    "collapse_all_windows", "check_all_windows",
    "clear_all", "ProtonVPN", "ActivateVPN",
    "collapse_all_windows", "Telegram"
]
full_screen = ["full_screen"]
main_group = ["main_group"]
close_all_windows = ["stop_all_BS_win", "yes_close_all"]

telegram_account_settings = "telegram_account_settings"


close_all_BS_window = [(350, 590), (500, 360)]

WIN_START = {
    "win0": {"cords": (540, 200)},
    "win1": {"cords": (540, 250)},
    "win2": {"cords": (540, 310)},
    "win3": {"cords": (540, 360)},
    "win4": {"cords": (540, 420)},
    "win5": {"cords": (540, 470)},
}

window_numbers = len(WIN_START)
# [Windows]---[End]

config = r'--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789/'

MAIN_DIR: Final[pathlib.Path] = pathlib.Path(__file__).parents[1]
