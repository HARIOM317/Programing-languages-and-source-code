from tkinter import *

def convert_size():
    WIDTH = window_width.get()
    HEIGHT = window_height.get()
    COLOR = root.config(background=window_color.get())
    size = root.geometry(f"{WIDTH}x{HEIGHT}")

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title("Modify The Window")

window_width = StringVar()
window_height = StringVar()
window_color = StringVar()

header_label = Label(root, text="The Window Size Converter Tool", font=("Poor Richard", 18, "bold", "underline"), fg="dark blue").place(x=35, y=10)

width_label = Label(root, text="Width", font=("Poor Richard", 14)).place(x=10, y=80)
height_label = Label(root, text="Height", font=("Poor Richard", 14)).place(x=10, y=110)
color_label = Label(root, text="Background", font=("Poor Richard", 14)).place(x=10, y=140)

entry_width = Entry(root, textvariable=window_width, width=30).place(x=150, y=80)
entry_height = Entry(root, textvariable=window_height, width=30).place(x=150, y=110)
entry_color = Entry(root, textvariable=window_color, width=30).place(x=150, y=140)

button = Button(root, text="Convert", command=convert_size, bg="sky blue").place(x=10, y=200)

root.mainloop()
