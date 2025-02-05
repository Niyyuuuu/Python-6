from tkinter import Tk
from tkinter.ttk import Progressbar

window = Tk()
progress = Progressbar(window, orient="horizontal", length=350, mode="determinate")
progress.pack()
progress["value"] = 80
window.mainloop()