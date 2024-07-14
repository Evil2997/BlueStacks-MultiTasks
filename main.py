import pathlib
import time
from typing import Final, Literal, List

import pyautogui as pg
from ahk import AHK

from modules.json_files import load_data
from modules.moves import Close_AnyWay, drag_to_bottom, drag_to_up
from modules.screens import find_it_and_click_it, scan_BUMP_daily_reward, hunt_for_the_button_in_list
from modules.Timers import delay
from modules.Timers import timer_checker as TIME_CHECK
from modules.Timers import timer_update as UPDATE_TIMER
from modules.windows import cycle_hunter_click, Stop_BS_Windows
from modules.windows import open_vpn_telegram as ACTIVATE_WINDOW
from modules.Timers import check_reward as CHECK_DAILY_REWARD
from modules.Timers import update_time_reward as UPDATE_TIME_DAILY_REWARD
from modules.games.game_512 import play_512

ahk = AHK()


# 3:45
def PreRun(finder,
           chat: bool = False,
           chat_type: Literal["image", "click"] = "image",
           chatbot_string: int = -1,
           chat_image_name: List[str] = None,
           threshold: float = 0.92):
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
            for _ in range(2):
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
        pg.click(click_diamonds)
    pg.press("num5")
    delay(10, 11)
    pg.press("num5")
    delay()
    pg.click(click_diamonds[0], click_diamonds[1] + 80)
    Close_AnyWay()


def Run_Clayton(dailik):
    how_much_you_want_to_play = 1
    PreRun(find_Clayton)
    if dailik:
        pg.click(claim_daily_reward)
        delay()
    for _ in range(2):
        pg.click(claim_coins)
        delay()
    play_512(how_much_you_want_to_play)
    Close_AnyWay()


def Run_BUMP(dailik):
    PreRun(find_BUMP, chat=True, chat_type="click", chatbot_string=0)
    scan_BUMP_daily_reward()
    delay(2, 3)
    for _ in range(2):
        find_it_and_click_it(green_X)
        delay(0.2, 0.5)
    for _ in range(16):
        pg.click(middle_screen)
        delay(0.2, 0.6)
    pg.press("num5")
    for _ in range(256):
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
        delay(0.4, 0.6)
        pg.click(get_reward_Fi)
    delay(0.2, 0.5)
    pg.click(cords_close)
    delay()
    drag_to_bottom()
    pg.click(middle_screen)
    Close_AnyWay()


def Run_HEXN(dailik):
    PreRun(find_HEXN)
    pg.click(claim_reward_HEXN)
    delay(3, 4)
    pg.click(start_farm_HEXN)
    Close_AnyWay()


def Run_DejenDog(dailik):
    PreRun(find_DejenDog, chat=True, chat_type="image", chat_image_name=ChatDog)
    pg.press("num3")
    delay(80, 90)
    pg.press("num3")
    drag_to_bottom()
    hunt_for_the_button_in_list(dog_lvlup_menu)
    delay()
    pg.click(Dog_LevelUp)
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
    find_it_and_click_it(Seeds_Check_news)
    delay()
    find_it_and_click_it(seeds_claim)
    delay()
    pg.click(caterpillar_claim_on_tree)
    delay()
    find_it_and_click_it(caterpillar_is_not_ready)
    find_it_and_click_it(sell_caterpillar)
    Close_AnyWay()


def Run_SimpleCoin(dailik):
    PreRun(find_SimpleCoin)
    for _ in range(2):
        delay()
        pg.click(claim_coins)
    find_it_and_click_it(fortuna_open)
    delay()
    pg.click(fortuna_run)
    delay(4, 5)
    find_it_and_click_it(fortuna_reward)
    find_it_and_click_it(fortuna_null_reward)
    delay()
    pg.click(cords_close)
    delay()
    pg.press("num3")
    delay(12, 15)
    pg.press("num3")
    Close_AnyWay()


def Run_BEE(dailik):
    for i in range(2):
        PreRun(find_BEE, chat=True, chat_type="click", chatbot_string=0)
        pg.press("num9")
        delay(7, 8)
        if i == 0:
            Close_AnyWay()
    hunt_for_the_button_in_list(upgrades_BEE)
    delay(0.2, 0.6)
    pg.press("num9")
    delay(7, 8)
    for stage in upgrades_BEE_stages:
        for _ in range(20):
            pg.click(stage)
            delay(0.6, 1)
    Close_AnyWay()


def Run_ElonMusk(dailik):
    PreRun(find_ElonMusk)
    hunt_for_the_button_in_list(Musk_take)
    Close_AnyWay()


def Run_TimeFarm(dailik):
    PreRun(find_TimeFarm)
    if dailik:
        pg.click(TimeFarm_daily_reward)
        delay()
    for _ in range(2):
        pg.click(FarmingTime)
        delay(3, 4)
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
    pg.click(Baboon_game_battery)
    pg.press("num4")
    delay(90, 100)
    pg.press("num4")
    for coordinates in repair_battery:
        pg.click(coordinates)
        delay(0.4, 0.8)
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
        while time.time() - time_start <= 20:
            find_it_and_click_it(Red_Tomato)
            delay(0.01, 0.04)
        delay(4, 5)
        pg.click(start_Tomato_game_again)
    Close_AnyWay()


def Run_Time_TON_Ecosystem(dailik):
    PreRun(find_Time_TON_Ecosystem, chat=True, chat_type="click", chatbot_string=2)
    for coordinates in Ecosystem_claim:
        pg.click(coordinates)
        delay(0.4, 0.8)
    Close_AnyWay()


def Run_TON_Station(dailik):
    PreRun(find_TON_Station)
    for coordinates in TON_Station_claim:
        pg.click(coordinates)
        delay(0.4, 0.6)
    Close_AnyWay()


def Run_Cyber_Finance(dailik):
    PreRun(find_Cyber_Finance, chat=True, chat_type="click", chatbot_string=2)
    for coordinates in upgrade_egg_hummer:
        pg.click(coordinates)
        delay(0.4, 0.6)
    cycle_hunter_click(hummer_accept_close)
    Close_AnyWay()


def Run_Fastmint(dailik):
    PreRun(find_Fastmint, chat=True, chat_type="click", chatbot_string=2)
    for coordinates in Fastmint_claim_and_farm:
        pg.click(coordinates)
        delay(0.4, 0.6)
    Close_AnyWay()


def Run_SnapSter(dailik):
    PreRun(find_SnapSter, chat=True, chat_type="click", chatbot_string=1)
    for coordinates in SnapSter_claim_and_farm:
        pg.click(coordinates)
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
        "Clayton": {"seconds": 28800, "function": Run_Clayton},
        "BUMP": {"seconds": 21600, "function": Run_BUMP},
        "PocketFi": {"seconds": 18000, "function": Run_PocketFi},
        "HEXN": {"seconds": 14400, "function": Run_HEXN},
        "DejenDog": {"seconds": 14400, "function": Run_DejenDog},
        "Seeds": {"seconds": 10800, "function": Run_Seeds},
        "SimpleCoin": {"seconds": 28800, "function": Run_SimpleCoin},
        "ElonMusk": {"seconds": 10800, "function": Run_ElonMusk},
        "BEE": {"seconds": 14400, "function": Run_BEE},
        "TimeFarm": {"seconds": 14400, "function": Run_TimeFarm},
        # "Baboon": {"seconds": 43200, "function": Run_Baboon},
        # "Tomato": {"seconds": Раз в сутки, "function": Run_Tomato},
        # "Time_TON_Ecosystem": {"seconds": 28800, "function": Run_Time_TON_Ecosystem},
        # "TON_Station": {"seconds": 28800, "function": Run_TON_Station},
        # "Cyber_Finance": {"seconds": 43200, "function": Run_Cyber_Finance},  # 86400
        # "Fastmint": {"seconds": 21600, "function": Run_Fastmint},
        # "SnapSter": {"seconds": 86400, "function": Run_SnapSter},
    }

    if True:
        number_bottom_drags = 64
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
        main_group = ["main_group"]
        # close_anyway = "close_anyway"

        click_to_bottom_in_BotChat = [(900, 880), (900, 800)]  # Add more if what need
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
        green_X = ["green_X"]
        click_at_moon = ["click_at_moon"]
        middle_screen = (960, 540)
        # [BUMP_params]-[End]

        # [PocketFi_params]-[Start]
        find_PocketFi = ["PocketFi"]
        # claim_switch = ["Claim_SWITCH"]
        get_daily_FiReward = ["FiQuests", "FiPresent"]
        get_reward_Fi = (940, 980)
        # [PocketFi_params]-[End]

        Dog_LevelUp = (800, 500)
        find_HEXN = ["HEXN"]
        find_DejenDog = ["DejenDog"]
        find_Seeds = ["Seeds"]
        find_SimpleCoin = ["SimpleCoin"]
        dog_lvlup_menu = ["dog_lvlup_menu"]
        seeds_claim = ["seeds_claim"]
        caterpillar_is_not_ready = ["caterpillar_is_not_ready"]
        caterpillar_claim_on_tree = (980, 560)
        fortuna_open = ["fortuna_open"]
        fortuna_run = (900, 900)
        fortuna_reward = ["fortuna_reward"]
        sell_caterpillar = ["sell_caterpillar"]
        ChatDog = ["ChatDog_Enter"]
        claim_reward_HEXN = (940, 880)
        start_farm_HEXN = (940, 840)
        Chat_open_BEE = (890, 890)
        full_screen_BEE = (1300, 500)
        upgrades_BEE = ["upgrades_BEE", "upgrades_BEE_2"]
        bee_lvl_up = ["bee_lvl_up"]
        upgrades_BEE_stages = [(1100, 550), (1100, 280)]
        Musk_take = ["Musk_take"]
        find_BEE = ["BEE"]
        find_ElonMusk = ["ElonMusk"]
        find_TimeFarm = ["TimeFarm"]
        FarmingTime = (1000, 800)
        TimeFarm_daily_reward = (1000, 980)
        Seeds_Daily = ["Seeds_Daily"]
        Got_It_Daily = ["Got_It_Daily"]
        Seeds_Check_news = ["Seeds_Check_news"]
        fortuna_null_reward = ["fortuna_null_reward"]
        daily_Seeds = [(1240, 440), (380, 530), (940, 530), (1500, 530), (380, 760), (940, 760), (1500, 760), (950, 750)]

    # ToDo: Set cords / make images
    find_Baboon = ["Baboon"]
    Baboon_daily_reward = [(), ()]
    combo_battery = [(), (), ()]
    bust_battery = [("click_bust_menu"), ("upgrade"), ("confirm")]
    repair_battery = [(), ()]
    Baboon_game_battery = ()

    find_Tomato = ["Tomato"]
    Tomato_claim_and_farm = ()
    play_Tomato = ()
    Red_Tomato = ["Red_Tomato"]
    start_Tomato_game_again = ()

    find_Time_TON_Ecosystem = ["Time_TON_Ecosystem"]
    Ecosystem_claim = [(), (), (), ()]

    find_TON_Station = ["TON_Station"]
    TON_Station_claim = [(), ()]

    find_Cyber_Finance = ["Cyber_Finance"]
    upgrade_egg_hummer = [(), ()]
    hummer_accept_close = ["hummer_accept", "hummer_close"]

    find_Fastmint = ["find_Fastmint"]
    Fastmint_claim_and_farm = [(), ()]

    find_SnapSter = ["SnapSter"]
    SnapSter_claim_and_farm = [(), ()]
    # [RUN_SCRIPT]-[START]
    main()
    # [RUN_SCRIPT]-[END]

    print("Время окончания сеанса:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
