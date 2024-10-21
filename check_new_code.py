import time

import cv2
import numpy as np
import pyautogui as pg
from mss import mss

from modules.Timers import delay
from modules.moves import drag_to_bottom


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


def trt():
    import json

    # Определение функций (они должны быть определены или импортированы в вашем коде)
    def Run_Blum():
        print("Running Blum")

    def Run_Diamond():
        print("Running Diamond")

    def Run_Clayton():
        print("Running Clayton")

    json_file = {"data.json": {
        "Blum": {"seconds": 28800, "function": "Run_Blum"},
        "Diamond": {"seconds": 28800, "function": "Run_Diamond"},
        "Clayton": {"seconds": 28800, "function": "Run_Clayton"}
    }
    }

    with open('data.json', 'r') as f:
        data = json.load(f)

    # Универсальный вызов функций
    for key, value in data.items():
        function_name = value["function"]

        # Предполагаем, что все функции находятся в этом же модуле
        function_to_call = globals().get(function_name)

        if function_to_call:
            function_to_call()  # Вызов функции
        else:
            print(f"Функция {function_name} не найдена.")


pass
pass
pass
pass
pass


def ere():
    drag_to_bottom()
    delay()
    pg.click()
    delay()

    scan()

    pass

def blum_clicker_game(target_colors,
                      region=(0, 0, 1920, 1080),
                      pixel_threshold=300,
                      tolerance=10,
                      ):

    x1, y1, x2, y2 = region
    monitor = {"top": y1, "left": x1, "width": x2 - x1, "height": y2 - y1}

    lower_bounds = np.clip(np.array(target_colors) - tolerance, 0, 255).astype(np.uint8)
    upper_bounds = np.clip(np.array(target_colors) + tolerance, 0, 255).astype(np.uint8)

    with mss() as sct:
        screenshot = np.array(sct.grab(monitor))
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

        masks = np.zeros(screenshot.shape[:2], dtype=np.uint8)

        for lower_bound, upper_bound in zip(lower_bounds, upper_bounds):
            mask = cv2.inRange(screenshot, lower_bound, upper_bound)
            masks = cv2.bitwise_or(masks, mask)
        cv2.imwrite("111.png", masks)
        white_pixels = np.column_stack(np.where(masks == 255))

        if len(white_pixels) > pixel_threshold:
            center_y, center_x = np.mean(white_pixels, axis=0).astype(int)
            pg.click(x1 + center_x, y1 + center_y)

        time.sleep(0.05)

def scan():
    colors_toxin = [
        (63, 219, 0), (122, 251, 36), (131, 254, 39), (197, 241, 1), (205, 222, 0), (229, 254, 144), (221, 221, 193),
        (182, 243, 123), (202, 254, 135), (228, 244, 124), (226, 255, 185), (128, 254, 40), (58, 203, 0),
        (131, 255, 39), (91, 233, 18), (45, 166, 1), (179, 245, 11), (59, 173, 13), (132, 255, 38), (177, 255, 68),
        (196, 252, 97), (185, 250, 100), (199, 239, 153), (216, 253, 167), (201, 246, 22),
    ]

    colors_freeze = [
        (86, 195, 210), (111, 215, 229), (85, 204, 220), (131, 220, 233), (85, 159, 220), (210, 226, 239),
        (170, 204, 233), (69, 136, 180),
    ]
    y_bounds = [(300, 540), (540, 780), (780, 1020)]

    time_start = time.time()
    for _ in range(1024):
        for y1, y2 in y_bounds:
            blum_clicker_game(
                    target_colors=colors_toxin,
                    region=(570, y1, 1310, y2),
                    pixel_threshold=600,
                    tolerance=30,
            )
            blum_clicker_game(
                    target_colors=colors_freeze,
                    region=(570, y1, 1310, y2),
                    pixel_threshold=400,
                    tolerance=30,
            )
        # if time_start-time.time() >= 32:
        #     break
        pass


scan()
