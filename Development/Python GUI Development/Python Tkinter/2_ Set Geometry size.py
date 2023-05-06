from tkinter import *

root = Tk()
'''
The Tkinter geometry specifies the method by using which, the widgets are represented on display. The python Tkinter provides the following geometry methods.

The pack() method
The grid() method
The place() method
'''

# Set Weigh x Height
root.geometry("600x400")
root.config(bg="light blue")        # Set the background color

# Set the minimum size of our window (Weigh , Height)
root.minsize(300, 150)

# Set the maximum size of our window (Weigh , Height)
root.maxsize(1000, 500)

# Create a label and pack them into geometry.
label1 = Label(text="Wellcome to Python", font=("Aparajita", 35, "bold"), fg="Red", bg="light blue")
label1.pack()
label1 = Label(text="Version 3.10.2", font=("Aparajita", 15), fg="dark blue", bg="light blue")
label1.pack()
label1 = Label(text="\nCreate New Project", font=("Aparajita", 20), fg="green", bg="light blue")
label1.pack()
label1 = Label(text="Open Project", font=("Aparajita", 20), fg="green", bg="light blue")
label1.pack()
label1 = Label(text="Check out from version control", font=("Aparajita", 20), fg="green", bg="light blue")
label1.pack()

root.mainloop()
