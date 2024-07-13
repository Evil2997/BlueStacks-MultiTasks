import json


def save_data(file_path, data):
    with open(file_path, 'w') as jf:
        json.dump(data, jf, indent=2)


def load_data(file_path):
    with open(file_path, 'r') as jf:
        return json.load(jf)
