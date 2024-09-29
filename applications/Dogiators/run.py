from applications import *
from applications.Dogiators import *
from modules.moves import Close_AnyWay


def Run_Dogiators(dailik, event, win_main):
    find_Dogiators = find_Dogiators_2 if win_main else find_Dogiators_1
    lines_numeric_to_upgrades = [1, 0]  # 1, 1, 0]
    upgrades_numeric = 2

    PreRun(
        find_Dogiators, win_main,
        initial_setup_clicker=True,
        initial_setup_images=pre_run_clicker
    )

    auto_get_telegram_subscribe_reward()

    started_pack()
    auto_clicker_Dogiator()

    pg.click(open_upgrades)
    delay()

    upgrades_Dogiators(
        lines_numeric_to_upgrades=lines_numeric_to_upgrades,
        upgrades_numeric=upgrades_numeric
    )

    auto_clicker_Dogiator()
    Close_AnyWay()


def auto_clicker_Dogiator(iteration_numbers=16):
    for _ in range(iteration_numbers):
        pg.press("num4")
        delay(4, 5)
        pg.press("num4")


def upgrades_Dogiators(lines_numeric_to_upgrades, upgrades_numeric=4):
    pg.click(open_upgrades)
    delay(3, 4)
    for i in range(upgrades_numeric):
        for ii, line in enumerate(lines_numeric_to_upgrades):
            from applications.Dogiators import upgrades_in_line
            upgrades_in_line = [upgrades_in_line[0]] if ii == 3 else upgrades_in_line

            for upgrade in upgrades_in_line:
                pg.click(upgrade)
                delay()
                pg.click(upgrade_click)
                delay(0.2, 0.5)
                pg.click(close_upgrade_Dogiator)
                delay(0.2, 0.5)
            if line == 1:
                pg.moveTo(Dogiators_drag_upgrades, duration=0.4)
                pg.dragTo(Dogiators_drag_upgrades[0], Dogiators_drag_upgrades[1] - pixels_drags, duration=0.6)
                delay(0.2, 0.5)
            delay(5, 6)
        for _ in range(len(lines_numeric_to_upgrades) * 2):
            drag_to_up(cords_to_drag=cords_to_drag_up_Dogiator)
        delay(3, 4)
    delay()
    pg.click(open_earn)
    delay(0.2, 0.5)


def started_pack():
    for _ in range(8):
        pg.click(open_earn)
        delay(0.6, 1)
    pg.click(close_upgrade_Dogiator)
    delay(0.02, 0.1)


def auto_get_telegram_subscribe_reward():
    if find_it_and_click_it(subscribe_on_telegram, threshold=0.86):
        for coordinates in subscribe:
            pg.click(coordinates)
            delay(2, 3)
