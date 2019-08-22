from tkinter import *
from tkinter import ttk
import subprocess
import os

def fireScript(*args):
    closeWindow()
    subprocess.call("./testClockIn.sh", shell=True)


def closeWindow():
    root.destroy()


root = Tk()
root.title("TimeClock")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

confirm = ttk.Button(mainframe, text="Confirm", command=fireScript).grid(column=1, row=3, sticky=W)
cancel = ttk.Button(mainframe, text="Cancel", command=closeWindow).grid(column=3, row=3, sticky=E)

ttk.Label(mainframe, text="Test this thing out?").grid(column=2, row=2, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

for btn in [confirm, cancel]:
  root.bind('<Return>', btn)

# root.attributes("-topmost", True)
root.mainloop()
