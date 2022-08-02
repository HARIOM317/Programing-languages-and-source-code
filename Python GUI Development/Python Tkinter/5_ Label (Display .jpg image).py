# Displaying .jpg Image using labels

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("1024x612")
root.resizable(0, 0)    # Fix the size

image = Image.open("A:\\Python GUI Development\\Python Tkinter\\Required Images\\1.jpg")
photo = ImageTk.PhotoImage(image)

Mylabel = Label(image=photo)
Mylabel.pack()

root.mainloop()

