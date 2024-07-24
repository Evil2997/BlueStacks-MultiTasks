import pathlib
import time
from typing import Final, Literal, List

import pyautogui as pg
from ahk import AHK

from games.game_512 import play_512
from modules.Timers import check_reward as CHECK_DAILY_REWARD
from modules.Timers import delay
from modules.Timers import timer_checker as TIME_CHECK
from modules.Timers import timer_update as UPDATE_TIMER
from modules.Timers import update_time_reward as UPDATE_TIME_DAILY_REWARD
from modules.json_files import load_data
from modules.moves import Close_AnyWay, drag_to_bottom, drag_to_up, auto_clicker
from modules.screens import find_it_and_click_it, scan_BUMP_daily_reward, hunt_for_the_button_in_list
from modules.windows import cycle_hunter_click, Stop_BS_Windows
from modules.windows import open_vpn_telegram as ACTIVATE_WINDOW

ahk = AHK()


def PreRun(finder,
           chat: bool = False,
           chat_type: Literal["image", "click"] = "image",
           chatbot_string: int = -1,
           chat_image_name: List[str] = None,
           threshold: float = 0.92
           ):
    if chat_type not in ["image", "click"]:
        raise ValueError("chat_type должен быть 'image' или 'click'")
    # [---Start---]
    for _ in range(16):
        if find_it_and_click_it(main_group):
            break
        delay(0.04, 0.6)
    for _ in range(number_bottom_drags):
        drag_to_bottom()
    while True:
        if not find_it_and_click_it(finder, threshold=threshold):
            drag_to_up()
        else:
            break
    if chat:
        delay(6, 8)
        if chat_type == "click":
            pg.click(click_to_bottom_in_BotChat[chatbot_string])
        elif chat_type == "image":
            cycle_hunter_click(chat_image_name)
    delay(16, 20)


def Run_Blum(dailik):
    PreRun(find_Blum)
    if dailik:
        pg.click(claim_reward_daily)
        delay(2, 3)
    for _ in range(2):
        pg.click(claim_farm)
        delay(2, 3)
    Close_AnyWay()

def Run_Diamond(dailik):
    PreRun(find_Diamond)
    if dailik:
        for coordinates in diamond_daily_reward:
            pg.click(coordinates)
            delay(0.4, 0.8)
        pg.press("Esc")
        delay()
        pg.click(diamond_game)
        delay()
    pg.press("num3")
    delay(10, 11)
    pg.press("num3")
    delay()
    pg.click(get_diamonds_reward_from_game)
    Close_AnyWay()


def Run_Clayton(dailik):
    how_much_you_want_to_play = 4
    PreRun(find_Clayton)
    if dailik:
        pg.click(claim_daily_reward)
        delay()
    drag_to_bottom(duration=0.4)
    for _ in range(4):
        pg.click(claim_coins)
        delay(0.5, 0.8)
    play_512(how_much_you_want_to_play)
    Close_AnyWay()


def Run_BUMP(dailik):
    PreRun(find_BUMP, chat=True, chat_type="click", chatbot_string=0)
    scan_BUMP_daily_reward()
    delay(2, 3)
    for _ in range(3):
        find_it_and_click_it(green_X)
        find_it_and_click_it(gray_X)
        delay(0.2, 0.5)
    for _ in range(16):
        pg.click(middle_screen)
        delay(0.2, 0.6)
    pg.press("num5")
    for _ in range(1000):
        is_it_clicked = find_it_and_click_it(click_at_moon)
        if is_it_clicked:
            pg.press("num5")
            break
        else:
            delay(0.01, 0.2)
    else:
        pg.press("num5")
    Close_AnyWay()


def Run_PocketFi(dailik):
    PreRun(find_PocketFi, threshold=0.7)
    drag_to_bottom()
    if dailik:
        hunt_for_the_button_in_list(get_daily_FiReward)
        delay()
        pg.click(get_reward_Fi)
    delay()
    pg.click(cords_close)
    delay()
    drag_to_bottom()
    pg.click(middle_screen)
    Close_AnyWay()


def Run_HEXN(dailik):
    PreRun(find_HEXN)
    for coordinates in rocket_time_reward:
        pg.click(coordinates)
        delay(0.4, 0.6)
    pg.press("Esc")
    delay()
    pg.click(claim_reward_HEXN)
    delay(4, 5)
    pg.click(start_farm_HEXN)
    Close_AnyWay()


def Run_DejenDog(dailik):
    PreRun(find_DejenDog, chat=True, chat_type="image", chat_image_name=ChatDog)
    pg.press("num3")
    delay(80, 90)
    pg.press("num3")
    for coordinates in dog_lvlup_menu:
        pg.click(coordinates)
        delay(8, 9)
    Close_AnyWay()


def Run_Seeds(dailik):
    PreRun(find_Seeds)
    if dailik:
        for coordinates in daily_Seeds:
            pg.click(coordinates)
            delay(0.4, 1)
            if coordinates == daily_Seeds[7]:
                drag_to_bottom()
                delay(0.2, 0.6)
    for coordinates in seeds_claim:
        pg.click(coordinates)
        delay(0.4, 1)
    pg.click(caterpillar_claim_on_tree)
    delay()
    find_it_and_click_it(caterpillar_is_not_ready)
    find_it_and_click_it(sell_caterpillar)
    Close_AnyWay()


def Run_SimpleCoin(dailik):
    PreRun(find_SimpleCoin)
    for _ in range(2):
        pg.click(claim_SimpleCoins)
        delay()
    pg.click(fortuna_open)
    delay()
    pg.click(fortuna_run)
    delay(4, 5)
    find_it_and_click_it(fortuna_reward)
    find_it_and_click_it(fortuna_null_reward)
    delay()
    pg.press("num3")
    delay(12, 15)
    pg.press("num3")
    Close_AnyWay()


def Run_BEE(dailik):
    for i in [0, 1]:
        PreRun(find_BEE, chat=True, chat_type="click", chatbot_string=2)
        drag_to_bottom(duration=0.6)
        delay()
        if i == 0:
            Close_AnyWay()
    for coordinates in upgrades_BEE:
        pg.click(coordinates)
        delay(0.01, 0.1)
    delay(8, 10)
    drag_to_bottom(duration=0.6)
    delay()
    for stage in upgrades_BEE_stages:
        for _ in range(20):
            pg.click(stage)
            delay(0.6, 1)
    Close_AnyWay()


def Run_ElonMusk(dailik):
    PreRun(find_ElonMusk)
    pg.click(Musk_take)
    if dailik:
        for coordinate in Elon_daily:
            pg.click(coordinate)
            delay(0.4, 0.8)
    Close_AnyWay()


def Run_TimeFarm(dailik):
    PreRun(find_TimeFarm)
    if dailik:
        pg.click(TimeFarm_daily_reward)
        delay()
    for _ in range(2):
        pg.click(FarmingTime)
        delay(6, 8)
    Close_AnyWay()


def Run_Baboon(dailik):
    PreRun(find_Baboon, chat=True, chat_type="click", chatbot_string=1)
    if dailik:
        for coordinates in Baboon_daily_reward:
            pg.click(coordinates)
            delay(0.4, 0.8)
        for battery in combo_battery:
            pg.click(battery)
            delay(0.4, 0.8)
        pg.press("Esc")
        delay()
    pg.press("num3")
    delay(90, 100)
    pg.press("num3")
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
                                if CHECK_DAILY_REWARD(window_number=i, game=game, rewards_file=rewards_file):
                                    UPDATE_TIME_DAILY_REWARD(window_numeric=i, game=game, rewards_file=rewards_file)
                        Stop_BS_Windows()
                        ACTIVATE = False
                time.sleep(600)
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
        # "Clayton": {"seconds": 28800, "function": Run_Clayton},
        # "BUMP": {"seconds": 21600, "function": Run_BUMP},
        # "PocketFi": {"seconds": 18000, "function": Run_PocketFi},
        # "HEXN": {"seconds": 14400, "function": Run_HEXN},
        # "DejenDog": {"seconds": 14400, "function": Run_DejenDog},
        # "Seeds": {"seconds": 10800, "function": Run_Seeds},
        # "SimpleCoin": {"seconds": 28800, "function": Run_SimpleCoin},
        # "ElonMusk": {"seconds": 10800, "function": Run_ElonMusk},
        # "BEE": {"seconds": 14400, "function": Run_BEE},
        # "TimeFarm": {"seconds": 14400, "function": Run_TimeFarm},
        # "Baboon": {"seconds": 43200, "function": Run_Baboon},
        # "Tomato": {"seconds": Раз в сутки, "function": Run_Tomato},
        # "Time_TON_Ecosystem": {"seconds": 28800, "function": Run_Time_TON_Ecosystem},
        # "TON_Station": {"seconds": 28800, "function": Run_TON_Station},
        # "Cyber_Finance": {"seconds": 7200, "function": Run_Cyber_Finance},  # 86400
        # "SnapSter": {"seconds": 86400, "function": Run_SnapSter},
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
        click_to_bottom_in_BotChat = [(900, 880), (900, 800), (900, 720)]
        # [names_for_images]---[END]

        #
        middle_screen = (960, 540)
        #

        # [Blum_params]-[Start]
        find_Blum = ["Blum"]
        claim_farm = (940, 840)
        claim_reward_daily = (750, 960)
        # [Blum_params]-[End]

        # [Diamond_params]-[Start]
        find_Diamond = ["Diamond"]
        get_diamonds_reward_from_game = (940, 820)
        diamond_daily_reward = [(1160, 340), (870, 480)]
        diamond_clicker = (940, 580)
        diamond_game = (720, 340)
        # [Diamond_params]-[End]

        # [Clayton_params]-[Start]
        find_Clayton = ["Clayton"]
        claim_daily_reward = (940, 840)
        claim_coins = (940, 720)
        # [Clayton_params]-[End]

        # [BUMP_params]-[Start]
        find_BUMP = ["BUMP"]
        green_X = ["green_X"]
        gray_X = ["gray_X"]
        click_at_moon = ["click_at_moon"]
        # [BUMP_params]-[End]

        # [PocketFi_params]-[Start]
        find_PocketFi = ["PocketFi"]
        get_daily_FiReward = ["FiQuests", "FiPresent"]
        get_reward_Fi = (940, 980)
        # [PocketFi_params]-[End]

        find_HEXN = ["HEXN"]
        rocket_time_reward = [(1440, 260),
                              (570, 330), (930, 330), (1300, 330),
                              (570, 570), (930, 570), (1300, 570),
                              (570, 800), (930, 800), (1300, 800)]
        claim_reward_HEXN = (940, 880)
        start_farm_HEXN = (940, 840)

        find_DejenDog = ["DejenDog"]
        ChatDog = ["ChatDog_Enter"]
        dog_lvlup_menu = [(880, 980), (800, 500)]


        find_Seeds = ["Seeds"]
        caterpillar_is_not_ready = ["caterpillar_is_not_ready"]
        sell_caterpillar = ["sell_caterpillar"]
        Got_It_Daily = ["Got_It_Daily"]
        seeds_claim = [(950, 750), (1200, 750)]
        caterpillar_claim_on_tree = (980, 560)
        daily_Seeds = [(1240, 440),
                       (380, 530), (940, 530), (1500, 530),
                       (380, 760), (940, 760), (1500, 760),
                       (950, 750)]

        find_SimpleCoin = ["SimpleCoin"]
        fortuna_reward = ["fortuna_reward"]
        fortuna_null_reward = ["fortuna_null_reward"]
        fortuna_open = (1700, 700)
        fortuna_run = (900, 900)
        claim_SimpleCoins = (920, 820)

        find_BEE = ["BEE"]
        upgrades_BEE = [(1150, 950), (1100, 950), (1200, 950)]
        upgrades_BEE_stages = [(1100, 860), (1100, 600), (1100, 320)]

        find_ElonMusk = ["ElonMusk"]
        Musk_take = (950, 950)
        Elon_daily = [(1600, 960), (1200, 580), (900, 910)]

        find_TimeFarm = ["TimeFarm"]
        FarmingTime = (940, 810)
        TimeFarm_daily_reward = (1000, 960)

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
