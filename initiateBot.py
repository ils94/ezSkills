import useFood
import useHeal
import switchTarget
import miscs


def initiate():
    miscs.multithreading(lambda: foodEater.eat)
    miscs.multithreading(lambda: healSpell.heal)
    miscs.multithreading(lambda: changeTarget.change_target)
