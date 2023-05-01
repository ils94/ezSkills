import threading


def multithreading(func):
    t = threading.Thread(target=func)
    t.setDaemon(True)
    t.start()
