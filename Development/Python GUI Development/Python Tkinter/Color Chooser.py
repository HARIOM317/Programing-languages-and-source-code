from tkinter import *
from tkinter import colorchooser

def select_color():
    color = colorchooser.askcolor(title="Select Color")
    root.config(bg=color[1])

root = Tk()
root.geometry('400x400')
button = Button(root, text="Choose Color", command=select_color)
button.pack()

root.mainloop()