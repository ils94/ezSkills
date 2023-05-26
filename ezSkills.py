from tkinter import Entry, Tk, X, LEFT, RIGHT, Checkbutton, IntVar, LabelFrame, Label, Button, END
import os
import globalVariables
import initiateBot
import saveConfig


def update_values():
    if var_target.get() == 1:
        globalVariables.switch_target_on = True
    else:
        globalVariables.switch_target_on = False

    if var_food.get() == 1:
        globalVariables.eat_food_on = True
    else:
        globalVariables.eat_food_on = False

    if var_health.get() == 1:
        globalVariables.use_heal_on = True
    else:
        globalVariables.use_heal_on = False

    globalVariables.char_name = entry_char_name.get()
    globalVariables.switch_target_key = entry_switch_target_hotkey.get()
    globalVariables.eat_food_key = entry_food_hotkey.get()
    globalVariables.use_heal_key = entry_health_hotkey.get()

    saveConfig.save_key_configs()


root = Tk()

var_target = IntVar()
var_food = IntVar()
var_health = IntVar()

window_width = 295
window_height = 75

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry("300x130+" + str(int(x)) + "+" + str(int(y)))
root.title("ezSkills")
if os.path.isfile("icon/pepeez.ico"):
    root.iconbitmap("icon/pepeez.ico")
root.resizable(False, False)

frame_char_name = LabelFrame(root, text="Character Name")
frame_char_name.pack(fill=X, padx=1, pady=1)

entry_char_name = Entry(frame_char_name)
entry_char_name.pack(fill=X, padx=1, pady=1)

frame_toggles = LabelFrame(root)
frame_toggles.pack(fill=X, padx=1, pady=1)

check_target = Checkbutton(frame_toggles, text="Switch Target", variable=var_target, onvalue=1, offvalue=0)
check_target.pack(side=LEFT)

check_f1 = Checkbutton(frame_toggles, text="Food", variable=var_food, onvalue=1, offvalue=0)
check_f1.pack(side=LEFT)

check_f2 = Checkbutton(frame_toggles, text="Health", variable=var_health, onvalue=1, offvalue=0)
check_f2.pack(side=LEFT)

frame_hotkeys = LabelFrame(root)
frame_hotkeys.pack(fill=X, padx=1, pady=1)

label_switch_target_hotkey = Label(frame_hotkeys, text="Target Key:", width=8)
label_switch_target_hotkey.pack(side=LEFT)

entry_switch_target_hotkey = Entry(frame_hotkeys, width=5)
entry_switch_target_hotkey.pack(side=LEFT)

label_food_hotkey = Label(frame_hotkeys, text="Food Key:", width=8)
label_food_hotkey.pack(side=LEFT)

entry_food_hotkey = Entry(frame_hotkeys, width=5)
entry_food_hotkey.pack(side=LEFT)

label_health_hotkey = Label(frame_hotkeys, text="Health Key:", width=8)
label_health_hotkey.pack(side=LEFT)

entry_health_hotkey = Entry(frame_hotkeys, width=5)
entry_health_hotkey.pack(side=LEFT)

button_update_values = Button(root, text="Update Values", width=15, command=update_values)
button_update_values.pack(side=RIGHT, padx=1, pady=1)

open_json_config = saveConfig.open_json_config()

entry_char_name.insert(END, open_json_config[0])

entry_switch_target_hotkey.insert(END, open_json_config[1])

entry_food_hotkey.insert(END, open_json_config[2])

entry_health_hotkey.insert(END, open_json_config[3])

initiateBot.initiate()

root.mainloop()
