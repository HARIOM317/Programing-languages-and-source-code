from tkinter import *


def trace():
    print(i.get())

root = Tk()
root.geometry('300x200')

i = StringVar()
cb = Checkbutton(root, text="Item 1", variable=i, offvalue="Button is Unchecked", onvalue="Button is Checked")
cb.pack()
Button(root, text="Trace", command=trace).pack()

root.mainloop()