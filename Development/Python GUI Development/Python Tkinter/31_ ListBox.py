'''
Todo :  The Listbox widget is used to display the list items to the user. We can place only text items in the Listbox and all text items contain the same font and color.
'''
from tkinter import *

def add():
    global i
    listbox.insert(ACTIVE, f"Item {i}")
    i += 1

i = 1
root =Tk()
root.geometry('200x200')
root.title("About List box")

listbox = Listbox(root)
listbox.pack()
listbox.insert(END, "Pen")

Button(root, text="Add Item", command=add).pack()

root.mainloop()
