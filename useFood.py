import windowsAPI
import time
import random
import virtualKeys
import globalVariables


def eat():
    while True:
        if globalVariables.eat_food_on:
            windowsAPI.send_keystrokes(virtualKeys.vk_code.get(globalVariables.eat_food_key))

            time.sleep(random.randint(0, 500))
