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
