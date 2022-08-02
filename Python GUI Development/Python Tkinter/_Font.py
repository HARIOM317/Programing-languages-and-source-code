from tkinter import *
from tkinter import font

root = Tk()
root.geometry('600x400')

available_Font_Family = list(font.families())
for item in available_Font_Family:
    print(item)

my_font = font.Font(family="Bahnschrift Light Condensed", size=50, weight='bold', slant='italic', underline=1, overstrike=1)
label = Label(root, text="Python Tkinter", font=my_font).pack()


root.mainloop()