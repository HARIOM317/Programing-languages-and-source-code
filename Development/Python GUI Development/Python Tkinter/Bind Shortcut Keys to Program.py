from tkinter import *
from tkinter import messagebox

def info(event=""):
    messagebox.showinfo("Information", "Shortcut key or button is working properly!")

root = Tk()
root.geometry('400x400')
Label(text="Note: Press ctrl.+i to shortcut!", font=("Comic Sans MS", 20, 'italic')).pack()
root.bind("<Control-i>", info)

Button(root, text='info', command=info, padx=30, pady=20, font="georgia 20 bold").pack()

root.mainloop()