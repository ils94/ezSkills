import windowsAPI
import time
import random
import virtualKeys
import globalVariables


def change_target(key1, key2, char_name):
    stance = [key1, key2]

    element = 0

    while True:
        if globalVariables.change_target_on:
            windowsAPI.send_keystrokes(virtualKeys.vk_code.get(stance[element]), char_name)

            element = element + 1

            if element > 1:
                element = 0

            time.sleep(random.randint(0, 180))
