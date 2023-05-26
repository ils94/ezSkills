import win32api
import win32con
import win32gui
import time
import globalVariables


def send_keystrokes(key):
    window = win32gui.FindWindow(None, "Tibia - " + globalVariables.char_name)

    win32api.SendMessage(window, win32con.WM_KEYDOWN, key, 0)
    time.sleep(0.5)
    win32api.SendMessage(window, win32con.WM_KEYUP, key, 0)
