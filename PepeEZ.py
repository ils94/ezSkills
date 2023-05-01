from tkinter import Button, Entry, Tk, X, RIGHT, LEFT, Checkbutton, IntVar, Menu
import miscs
import os
import helpWindow
import start_bot

root = Tk()

var_target = IntVar()
var_f1 = IntVar()
var_f2 = IntVar()
var_def_bal = IntVar()

window_width = 300
window_height = 50

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry("300x70+" + str(int(x)) + "+" + str(int(y)))
root.title("Pepe EZ")
if os.path.isfile("icon/pepeez.ico"):
    root.iconbitmap("icon/pepeez.ico")
root.resizable(False, False)

menu_bar = Menu(root)

menu = Menu(menu_bar, tearoff=0)

menu.add_command(label="Help", command=lambda: helpWindow.open_help())

menu_bar.add_cascade(label="Menu", menu=menu)

root.config(menu=menu_bar)

entry_char_name = Entry()
entry_char_name.pack(fill=X, padx=2, pady=2)

button_start = Button(root, text="Start", width=5, height=1, command=lambda: miscs.multithreading(lambda:
                                                                                                  start_bot.start(
                                                                                                      entry_char_name.get(),
                                                                                                      button_start,
                                                                                                      var_target,
                                                                                                      var_f1,
                                                                                                      var_f2,
                                                                                                      var_def_bal)))
button_start.pack(side=RIGHT, padx=2, pady=2)

check_target = Checkbutton(root, text="Switch Target", variable=var_target, onvalue=1, offvalue=0)
check_target.pack(side=LEFT)

check_f1 = Checkbutton(root, text="F1", variable=var_f1, onvalue=1, offvalue=0)
check_f1.pack(side=LEFT)
var_f1.set(1)

check_f2 = Checkbutton(root, text="F2", variable=var_f2, onvalue=1, offvalue=0)
check_f2.pack(side=LEFT)
var_f2.set(1)

check_def_bal = Checkbutton(root, text="Def/Bal", variable=var_def_bal, onvalue=1, offvalue=0)
check_def_bal.pack(side=LEFT)
var_def_bal.set(1)

if os.path.isfile("character.txt"):
    f = open("character.txt", "r")

    entry_char_name.insert(0, f.read())

root.mainloop()
