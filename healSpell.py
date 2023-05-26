import globalVariables
import windowsAPI
import time
import random
import virtualKeys


def heal(key, char_name):
    while True:
        if globalVariables.use_heal_on:
            windowsAPI.send_keystrokes(virtualKeys.vk_code.get(key), char_name)

            time.sleep(random.randint(0, 500))
