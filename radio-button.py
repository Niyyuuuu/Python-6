from tkinter import Tk, Radiobutton, IntVar

window = Tk()
var = IntVar()
Radiobutton(window, text="ITB", variable=var, value=1).pack()
Radiobutton(window, text="UI", variable=var, value=2).pack()
window.mainloop()
