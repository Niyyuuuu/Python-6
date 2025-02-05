from tkinter import Tk, Scrollbar, Text

window = Tk()

scrollbar = Scrollbar(window)
scrollbar.pack(side="right", fill="y")

text = Text(window, wrap="none", yscrollcommand=scrollbar.set)
text.pack(side="left", fill="both", expand=True)

scrollbar.config(command=text.yview)

window.mainloop()