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

def deedeed():
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
