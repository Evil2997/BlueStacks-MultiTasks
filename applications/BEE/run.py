from applications import *
from applications.BEE import *
from modules.Text_workers import fff
from modules.moves import Close_AnyWay
from modules.screens import click_on_images


def Run_BEE(dailik, event, win_main):
    find_BEE = find_BEE_2 if win_main else find_BEE_1

    PreRun(find_BEE, win_main, chat=True, chat_type="click", chatbot_string=2)

    get_dailik()
    upgrade_stage_1()
    upgrade_stage_2()
    Close_AnyWay()


def get_dailik():
    if click_on_images(target_colors=colors_check_daily):
        pg.click(daily_BEE)
        delay()


def upgrade_stage_1():
    pg.click(upgrades_BEE)
    delay()
    for _ in range(3):
        drag_to_bottom(duration=0.2)
        delay(0.2, 0.3)
    for _ in range(10):
        for coordinates in upgrades_all:
            pg.click(coordinates)
            delay(0.02, 0.2)
        delay(0.25, 0.5)


def upgrade_stage_2():
    pg.click(other_menu_BEE)
    delay(3, 4)
    pg.click(upgrades_BEE)
    for _ in range(10):
        pg.click(upgrades_last)
        delay(0.6, 0.8)


def find_the_best_upgrade_to_improve():
    # [4 - 3 - 2]
    pg.click(upgrades_BEE)
    delay()
    for _ in range(3):
        drag_to_bottom(duration=0.2)
        delay(0.2, 0.3)
    # [4 - 3 - 2]

    pg.click(other_menu_BEE)
    delay(3, 4)

    # [1 - 2]
    pg.click(upgrades_BEE)
    # [1 - 2]
    pass


def calculate_efficiency(delta_p, cost):
    """
    Рассчитывает эффективность апгрейда.

    :param delta_p: Текущая стоимость
    :param cost: Соотношение стоимости
    :return: Эффективность апгрейда
    """
    return delta_p / cost


def find_best_upgrade(delta_p_values, cost_factors):
    """
    Определяет, какой апгрейд является наиболее выгодным.

    :param delta_p_values: Список приростов параметров для каждого апгрейда
    :param cost_factors: Список факторов стоимости для каждого апгрейда
    :return: Индекс наиболее выгодного апгрейда
    """
    efficiencies = [
        calculate_efficiency(delta_p, cost)
        for delta_p, cost in zip(delta_p_values, cost_factors)
    ]
    best_upgrade_index = efficiencies.index(max(efficiencies))
    return best_upgrade_index, efficiencies


def f1():
    BEE_honey_cost = "BEE_honey_cost"
    fff(BEE_honey_cost)
    delta_p_values = [10, 20, 30, 35]  # Прирост параметров для 4-х способностей
    cost_factors = [1, 3, 6, 10]  # Факторы стоимости для 4-х способностей

    # Поиск наиболее выгодного апгрейда
    best_upgrade_index, efficiencies = find_best_upgrade(delta_p_values, cost_factors)

    # Вывод результата
    print(f"Эффективности апгрейдов: {efficiencies}")
    print(f"Наиболее выгодный апгрейд: способность {best_upgrade_index + 1}")
