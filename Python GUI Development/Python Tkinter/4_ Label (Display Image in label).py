# Displaying Image using labels

from tkinter import *

root = Tk()
root.geometry("200x175")
root.resizable(0, 0)    # Fix the size
photo = PhotoImage(file="A:\\Python GUI Development\\Python Tkinter\\Required Images\\1.png")       # This will work for only .png images
Mylabel = Label(image=photo)
Mylabel.pack()

root.mainloop()
