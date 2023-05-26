import win32api
import win32con
import win32gui
import time


def send_keystrokes(key, char_name):
    window = win32gui.FindWindow(None, "Tibia - " + char_name)

    win32api.SendMessage(window, win32con.WM_KEYDOWN, key, 0)
    time.sleep(0.5)
    win32api.SendMessage(window, win32con.WM_KEYUP, key, 0)
