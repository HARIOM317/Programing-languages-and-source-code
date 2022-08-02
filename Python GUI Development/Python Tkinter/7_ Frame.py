# It can be defined as a container to which, another widget can be added and organized.
from tkinter import *
root = Tk()
root.geometry("150x100")
root.resizable(0, 0)

frame = Frame(root)
frame.pack()

leftFrame = Frame(root)
leftFrame.pack(side=LEFT)

rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)

button1 = Button(frame, text="Submit", fg="Red", activebackground="Red")
button1.pack(side=LEFT)
button2 = Button(frame, text="Remove", fg="brown", activebackground="brown", cursor="circle")
button2.pack(side=RIGHT)
button3 = Button(rightFrame, text="Add", fg="blue", activebackground="sky blue", cursor="plus")
button3.pack(side=LEFT)
button4 = Button(leftFrame, text="Modify", fg="black", activebackground="white", cursor="dot")
button4.pack(side=RIGHT)

root.mainloop()
