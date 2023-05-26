import useFood
import useHeal
import switchTarget
import miscs


def initiate():

    miscs.multithreading(lambda: useFood.eat())
    miscs.multithreading(lambda: useHeal.heal())
    miscs.multithreading(lambda: switchTarget.change_target())
