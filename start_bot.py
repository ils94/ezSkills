from tkinter import messagebox
import time
import win32api
import win32con
import win32gui
import random


def start(char_name, button_start, var_target, var_f1, var_f2, var_def_bal):
    window = win32gui.FindWindow(None, "Tibia - " + char_name)

    with open("character.txt", "w") as f:
        f.write(char_name)

    if char_name == "":
        messagebox.showerror("Error", "You must provide the name of your character, dude.")
    else:

        button_start["state"] = "disabled"

        stance = [0x72, 0x73]

        element = 0

        while True:

            if var_target.get():
                win32api.SendMessage(window, win32con.WM_KEYDOWN, 0x20, 0)
                win32api.SendMessage(window, win32con.WM_KEYUP, 0x20, 0)

                time.sleep(random.uniform(0, 3))

            if var_f1.get():
                win32api.SendMessage(window, win32con.WM_KEYDOWN, 0x70, 0)
                win32api.SendMessage(window, win32con.WM_KEYUP, 0x70, 0)

                time.sleep(random.uniform(0, 3))

            if var_f2.get():
                win32api.SendMessage(window, win32con.WM_KEYDOWN, 0x71, 0)
                win32api.SendMessage(window, win32con.WM_KEYUP, 0x71, 0)

                time.sleep(random.uniform(0, 3))

            if var_def_bal.get():

                win32api.SendMessage(window, win32con.WM_KEYDOWN, stance[element], 0)
                win32api.SendMessage(window, win32con.WM_KEYUP, stance[element], 0)

                element = element + 1

                if element < 1:
                    element = 0

            time.sleep(random.uniform(120, 180))
