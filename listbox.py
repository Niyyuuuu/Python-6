from tkinter import *
window = Tk()
listbox = Listbox(window)
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.pack()
window.mainloop()