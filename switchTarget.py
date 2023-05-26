import windowsAPI
import time
import random
import virtualKeys
import globalVariables


def change_target():
    while True:
        if globalVariables.change_target_on:
            windowsAPI.send_keystrokes(virtualKeys.vk_code.get(globalVariables.change_target_key))

            time.sleep(random.randint(0, 180))
