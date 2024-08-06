import pathlib
import time
from typing import Final, Literal, List

import pyautogui as pg
from ahk import AHK

from modules.Timers import check_reward as CHECK_DAILY_REWARD
from modules.Timers import delay
from modules.Timers import timer_checker as TIME_CHECK
from modules.Timers import timer_update as UPDATE_TIMER
from modules.Timers import update_time_reward as UPDATE_TIME_DAILY_REWARD
from modules.json_files import load_data
from modules.moves import Close_AnyWay, drag_to_bottom, drag_to_up, swipe_right, swipe_left
from modules.screens import find_it_and_click_it, scan_BUMP_daily_reward, hunt_for_the_button_in_list, \
    find_template_on_region
from modules.windows import cycle_hunter_click, Stop_BS_Windows
from modules.windows import activate_window as ACTIVATE_WINDOW
from special_events.game_512 import play_512

# from special_events.BUMB_bust import buy_bust

ahk = AHK()


def primary_hunter_click(finder, threshold):
    MAIN_CYCLE = True
    while MAIN_CYCLE:
        if not MAIN_CYCLE:
            break
        find_it_and_click_it(main_group)
        for _ in range(3):
            delay(0.4, 0.6)
            pg.click(close_main_group)
        delay(4, 5)
        find_it_and_click_it(main_group)
        for _ in range(20):
            if not MAIN_CYCLE:
                break
            if find_template_on_region(bug_while_scrolling_chat):
                pg.click(close_main_group)
                find_it_and_click_it(main_group)
            for _ in range(20):
                if find_it_and_click_it(finder, threshold=threshold):
                    MAIN_CYCLE = False
                    break
                else:
                    drag_to_up()


def PreRun(finder,
           chat: bool = False,
           chat_type: Literal["image", "click"] = "click",
           chatbot_string: int = -1,
           chat_image_name: List[str] = None,
           threshold: float = 0.92
           ):
    if chat_type not in ["image", "click"]:
        raise ValueError("chat_type должен быть 'image' или 'click'")
    # [---Start---]
    for _ in range(16):
        if find_it_and_click_it(main_group):
            find_it_and_click_it(main_group)
            break
        delay(0.04, 0.6)
    drag_to_bottom()

    primary_hunter_click(finder=finder, threshold=threshold)

    if chat:
        delay(8, 10)
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
    for i in [0, 1]:
        pg.press("num4")
        delay(12, 14)
        pg.press("num4")
        delay()
        pg.click(get_diamonds_reward_from_game)
        delay()
        if i == 0:
            pg.click(get_diamonds_reward_from_game)
            delay(16, 20)
    if dailik:
        for coordinates in diamond_daily_reward:
            pg.click(coordinates)
            delay()
    Close_AnyWay()


def Run_Clayton(dailik):
    how_much_you_want_to_play = 2
    PreRun(find_Clayton)
    if dailik:
        pg.click(claim_daily_reward)
        delay()
    drag_to_bottom(duration=0.4)
    for _ in range(4):
        pg.click(claim_coins)
        delay(0.5, 0.8)
    # play_512(how_much_you_want_to_play)
    Close_AnyWay()


def Run_BUMP(dailik):
    PreRun(find_BUMP, chat=True, chat_type="click", chatbot_string=0)
    scan_BUMP_daily_reward()
    delay(2, 3)
    for _ in range(3):
        find_it_and_click_it(green_X)
        find_it_and_click_it(gray_X)
        delay(0.2, 0.5)
        for _ in range(2):
            swipe_left()
            delay(0.2, 0.5)
    # BUST
    # delay()
    # buy_bust()
    # BUST
    for _ in range(16):
        pg.click(middle_screen)
        delay(0.2, 0.6)
    pg.press("num4")
    for _ in range(256):
        is_it_clicked = find_it_and_click_it(click_at_moon)
        if is_it_clicked:
            pg.press("num4")
            break
        else:
            delay(0.01, 0.2)
    else:
        pg.press("num4")
    Close_AnyWay()


def Run_PocketFi(dailik):
    PreRun(find_PocketFi, threshold=0.7)
    for coordinates in mining_fi:
        pg.click(coordinates)
        delay()
    if dailik:
        for coordinates in get_daily_FiReward:
            pg.click(coordinates)
            delay(0.4, 1)
    pg.click(claim_switch)
    Close_AnyWay()


def Run_HEXN(dailik):
    PreRun(find_HEXN)
    for coordinates in claim_reward_HEXN:
        pg.click(coordinates)
        delay(6, 8)
    for coordinates in rocket_time_reward:
        pg.click(coordinates)
        delay(0.4, 0.6)
    Close_AnyWay()


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


def Run_Seeds(dailik):
    PreRun(find_Seeds)
    if dailik:
        pg.click(open_daily_Seeds)
        delay(3, 4)
        drag_to_bottom(duration=0.4, cords_to_drag=(940, 300))
        for coordinates in daily_Seeds:
            pg.click(coordinates)
            delay(0.2, 0.6)
        drag_to_up(duration=0.4, cords_to_drag=(940, 300))
        pg.click(claim_ticket_Seeds)
        pg.press("Esc")
        delay()
        for coordinates in get_ticket_Seeds:
            pg.click(coordinates)
            delay(6, 8)
        pg.press("Esc")
        delay()
    for coordinates in seeds_claim:
        pg.click(coordinates)
        delay(0.4, 1)
    for _ in range(2):
        pg.click(caterpillar_claim_on_tree)
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
    pg.press("num2")
    delay(12, 15)
    pg.press("num2")
    Close_AnyWay()


def Run_BEE(dailik):
    PreRun(find_BEE, chat=True, chat_type="click", chatbot_string=2)
    drag_to_bottom(duration=0.6)
    delay()
    # BEE_check_daily()
    pg.click(daily_BEE)
    delay(3, 4)
    for coordinates in upgrades_BEE:
        pg.click(coordinates)
        delay(0.01, 0.1)
    delay(8, 10)
    for _ in range(3):
        drag_to_bottom(duration=0.33)
        delay()
    for i, stage in enumerate(upgrades_BEE_stages):
        if i == 3:
            pg.click(other_menu_BEE)
            delay()
            for coordinates in upgrades_BEE:
                pg.click(coordinates)
                delay(0.01, 0.1)
            delay(4, 5)
        for _ in range(20):
            pg.click(stage)
            delay(0.6, 1)
    Close_AnyWay()


def Run_ElonMusk(dailik):
    PreRun(find_ElonMusk)
    pg.click(Musk_take)
    delay(4, 5)
    if dailik:
        for coordinate in Elon_daily:
            pg.click(coordinate)
            delay(4, 5)
    Close_AnyWay()


def Run_TimeFarm(dailik):
    PreRun(find_TimeFarm, chat=True, chat_type="click", chatbot_string=1)
    for coordinates in FarmingTime:
        pg.click(coordinates)
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
        "HEXN": {"seconds": 7200, "function": Run_HEXN},
        "DejenDog": {"seconds": 14400, "function": Run_DejenDog},
        "Seeds": {"seconds": 14400, "function": Run_Seeds},
        "SimpleCoin": {"seconds": 28800, "function": Run_SimpleCoin},
        # "ElonMusk": {"seconds": 10800, "function": Run_ElonMusk},
        "BEE": {"seconds": 14400, "function": Run_BEE},
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
        click_to_bottom_in_BotChat = [(890, 880), (890, 800), (890, 720)]
        # [names_for_images]---[END]

        #
        middle_screen = (960, 540)
        close_main_group = (730, 130)
        bug_while_scrolling_chat = "bug_while_scrolling_chat"
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
        claim_daily_reward = (920, 870)
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
        mining_fi = [(1570, 240), (940, 930)]
        get_daily_FiReward = [(830, 930), (940, 720), (940, 990), (1000, 220), (940, 930)]
        claim_switch = (940, 720)
        # [PocketFi_params]-[End]

        find_HEXN = ["HEXN"]
        rocket_time_reward = [(1440, 260),
                              (570, 330), (930, 330), (1300, 330),
                              (570, 570), (930, 570), (1300, 570),
                              (570, 800), (930, 800), (1300, 800)]
        claim_reward_HEXN = [(240, 940), (940, 820), (940, 820)]
        agree_new_updates = (940, 940)

        find_DejenDog = ["DejenDog"]
        ChatDog = ["ChatDog_Enter"]
        dog_lvlup_menu = [(940, 950), (800, 440)]

        find_Seeds = ["Seeds"]
        seeds_claim = [(950, 750), (1200, 750)]
        caterpillar_claim_on_tree = (980, 660)
        open_daily_Seeds = (1240, 540)
        daily_Seeds = [(720, 370), (940, 370), (1200, 370),
                       (720, 590), (940, 590), (1200, 590),
                       (940, 800)]
        claim_ticket_Seeds = (940, 500)
        get_ticket_Seeds = [(1240, 630), (1080, 900)]

        find_SimpleCoin = ["SimpleCoin"]
        fortuna_reward = ["fortuna_reward"]
        fortuna_null_reward = ["fortuna_null_reward"]
        fortuna_open = (1700, 700)
        fortuna_run = (900, 900)
        claim_SimpleCoins = (920, 820)

        find_BEE = ["BEE"]
        daily_BEE = (950, 980)
        upgrades_BEE = [(1150, 950), (1100, 950), (1200, 950)]
        upgrades_BEE_stages = [(1090, 810), (1090, 540), (1090, 270), (1090, 700)]
        other_menu_BEE = (290, 950)

        find_ElonMusk = ["ElonMusk"]
        Musk_take = (950, 950)
        Elon_daily = [(1600, 960), (1200, 580), (900, 950)]

        find_TimeFarm = ["TimeFarm"]
        FarmingTime = [(160, 950), (940, 810), (940, 810)]

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
