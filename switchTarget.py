import windowsAPI
import time
import random
import virtualKeys
import globalVariables


def change_target():
    while True:
        if globalVariables.switch_target_on and globalVariables.switch_target_key:

            time.sleep(random.randint(4, 5))

            windowsAPI.send_keystrokes(virtualKeys.vk_code.get(globalVariables.switch_target_key))

            tick = random.randint(0, 180)

            while tick:
                if globalVariables.switch_target_on:
                    tick = tick - 1
                    time.sleep(1)
                else:
                    break

        time.sleep(0.5)
