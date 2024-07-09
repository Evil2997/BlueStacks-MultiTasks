import pathlib
from typing import Final


def CHECK_TIME():
    import time

    time_start = time.time()
    hours_to_wait = 8

    while True:
        elapsed_time = (time.time() - time_start) / 3600
        remaining_time = hours_to_wait - elapsed_time

        if remaining_time <= 0:
            print("Время ожидания закончилось!")
            break

        remaining_hours = int(remaining_time)
        remaining_minutes = int((remaining_time - remaining_hours) * 60)
        remaining_minutes = f"{remaining_minutes:02d}"

        print(f"Осталось ждать: {remaining_hours}:{remaining_minutes}")
        time.sleep(3)


def RANDOM_MOVE():
    import random
    import pyautogui as pg

    def get_random_direction():
        directions = {
            0: "вверх",
            1: "вниз",
            2: "влево",
            3: "вправо"
        }
        # Генерируем случайное число от 0 до 3
        random_value = random.randint(0, 3)

        # Возвращаем направление движения
        return directions[random_value]

    def move_random_direction():
        direction = get_random_direction()

        screen_width, screen_height = pg.size()
        current_x, current_y = pg.position()

        if direction == "вверх":
            pg.moveTo(current_x, current_y - 100)
            pg.dragTo(current_x, current_y)
        elif direction == "вниз":
            pg.moveTo(current_x, current_y + 100)
            pg.dragTo(current_x, current_y)
        elif direction == "влево":
            pg.moveTo(current_x - 100, current_y)
            pg.dragTo(current_x, current_y)
        elif direction == "вправо":
            pg.moveTo(current_x + 100, current_y)
            pg.dragTo(current_x, current_y)

    # Пример использования функции
    for _ in range(10):
        move_random_direction()


def WINDOWS_PARAMS():
    # [windows_params]-[START]
    A = 871
    B = 872
    Q = 509
    R = 510
    Z = 0
    WIN_CORDS = {
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
        # ===================================================== #
        "win4": {"Win_Name": "BlueStacks 4",
                 "X": Z, "Y": Z, "WIDTH": A, "HEIGHT": Q,
                 "region": (Z, Z, A, Q)},
        "win5": {"Win_Name": "BlueStacks 5",
                 "X": B, "Y": Z, "WIDTH": A, "HEIGHT": Q,
                 "region": (B, Z, B + A, Q)},
        "win6": {"Win_Name": "BlueStacks 6",
                 "X": Z, "Y": R, "WIDTH": A, "HEIGHT": Q,
                 "region": (Z, R, A, Q + R)},
        "win7": {"Win_Name": "BlueStacks 7",
                 "X": B, "Y": R, "WIDTH": A, "HEIGHT": Q,
                 "region": (B, R, B + A, Q + R)},
    }
    WIN_NUMBERS = 5
    # [windows_params]-[END]


