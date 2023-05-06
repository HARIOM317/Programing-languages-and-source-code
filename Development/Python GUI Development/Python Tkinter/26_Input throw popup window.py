from tkinter import *
from tkinter import simpledialog
def PopUp_Window():
    s = simpledialog.askstring("Input Name", "Enter your name")
root = Tk()
root.geometry('200x200')
Button(root, text='Click Me', command=PopUp_Window).pack()
root.mainloop()