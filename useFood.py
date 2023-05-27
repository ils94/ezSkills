import windowsAPI
import time
import random
import virtualKeys
import globalVariables


def eat():
    while True:
        if globalVariables.eat_food_on and globalVariables.eat_food_key:

            time.sleep(random.randint(0, 1))

            windowsAPI.send_keystrokes(virtualKeys.vk_code.get(globalVariables.eat_food_key))

            tick = random.randint(120, 240)

            while tick:
                if globalVariables.eat_food_on:
                    tick = tick - 1
                    time.sleep(1)
                else:
                    break

        time.sleep(0.5)
