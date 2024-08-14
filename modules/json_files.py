import json


def save_data(file_path, data):
    with open(file_path, 'w') as jf:
        json.dump(data, jf, indent=2)


def load_data(file_path):
    with open(file_path, 'r') as jf:
        return json.load(jf)


def align_json_values(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    aligned_data = {outer_key: align_dict_values(inner_dict) for outer_key, inner_dict in data.items()}

    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump(aligned_data, output_file, ensure_ascii=False, indent=4)

    # Дополнительное форматирование для выравнивания значений
    with open(output_path, 'r', encoding='utf-8') as output_file:
        lines = output_file.readlines()

    with open(output_path, 'w', encoding='utf-8') as output_file:
        max_length = max(len(line.split(':')[0]) for line in lines if ':' in line)
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                output_file.write(f"{key.strip():<{max_length}}: {value}")
            else:
                output_file.write(line)


def align_dict_values(d):
    # Возвращает словарь, отсортированный по ключам
    return {k: d[k] for k in sorted(d)}

