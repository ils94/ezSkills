import foodEater
import healSpell
import changeTarget
import miscs


def initiate(key1, key2, char_name):
    miscs.multithreading(lambda: foodEater.eat(key1, char_name))
    miscs.multithreading(lambda: healSpell.heal(key1, char_name))
    miscs.multithreading(lambda: changeTarget.change_target(key1, key2, char_name))
