import windowsAPI
import time
import random
import virtualKeys
import globalVariables


def eat(key, char_name):
    while True:
        if globalVariables.eat_food_on:
            windowsAPI.send_keystrokes(virtualKeys.vk_code.get(key), char_name)

            time.sleep(random.randint(0, 500))
