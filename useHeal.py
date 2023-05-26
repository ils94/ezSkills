import globalVariables
import windowsAPI
import time
import random
import virtualKeys


def heal():
    while True:
        if globalVariables.use_heal_on:
            windowsAPI.send_keystrokes(virtualKeys.vk_code.get(globalVariables.use_heal_key))

            time.sleep(random.randint(0, 500))
