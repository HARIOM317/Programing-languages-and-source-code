# The Button is used to add various kinds of buttons to the python application.
from tkinter import *
root = Tk()
root.geometry('150x200')

b1 = Button(root, text="Home")
b1.pack()
b2 = Button(root, text="Forward")
b2.pack()
b3 = Button(root, text="Backward")
b3.pack()
b4 = Button(root, text="Recent")
b4.pack()
b5 = Button(root, text="History")
b5.pack()

close_Button = Button(root, text="Close", command=root.destroy).pack()

root.mainloop()
