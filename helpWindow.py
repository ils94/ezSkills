from tkinter import Tk, Label, BOTH, LEFT


def open_help():
    help_window = Tk()
    help_window.title("Help")
    help_window.resizable(False, False)

    help_label = Label(help_window, text="How to use this tool:"
                                         "\n\n•Configure the buttons F1 and F2 for either food and heal;"
                                         "\n•Configure the F3 button to change to your Defense Stance;"
                                         "\n•Configure the F4 button to change to your Balance Stance."
                                         "\n\nThe Switch Target is used to change between monsters "
                                         "\nto help mitigate the chances of killing one of them during"
                                         "\nthe training session."
                                         "\n\nYou can uncheck the Switch Target, F1, F2 and Def/Bal "
                                         "\nboxes to ignore them."
                                         "\n\nThis tool does not inject anything into Tibia Client, it just"
                                         "\nsend keystrokes direct to the application and nothing else."
                                         "\n\nDo not leave your character training 100% afk, don't be stupid."
                                         "\n\nThis tool is more so you don't get logged off after 15 minutes AFK.",
                       anchor="w", justify=LEFT)
    help_label.pack(fill=BOTH, padx=5, pady=5)

    help_window.mainloop()
