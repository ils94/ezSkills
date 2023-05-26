import json
import os
import globalVariables


def create_json_config(value1, value2, value3, value4):
    data = {
        "value1": value1,
        "value2": value2,
        "value3": value3,
        "value4": value4,
    }

    with open("config.json", "w") as json_file:
        json.dump(data, json_file)


def open_json_config():
    try:
        file_path = "config.json"

        if os.path.exists(file_path):
            with open(file_path, "r") as json_file:
                data = json.load(json_file)

                value1 = data['value1']
                value2 = data['value2']
                value3 = data['value3']
                value4 = data['value4']

                return value1, value2, value3, value4
        else:
            return "", "", "", ""
    except Exception as e:
        print(e)
        os.remove("config.json")
        return "", "", "", ""


def save_key_configs():
    char_name = globalVariables.char_name
    switch_target_key = globalVariables.switch_target_key
    use_food_key = globalVariables.eat_food_key
    use_heal_key = globalVariables.use_heal_key

    create_json_config(char_name, switch_target_key, use_food_key, use_heal_key)
