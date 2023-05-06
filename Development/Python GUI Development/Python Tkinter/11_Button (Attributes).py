'''
A list of possible options is given below.

SN	Option	Description
1.	activebackground -->	It represents the background of the button when the mouse hover the button.
2.	activeforeground -->	It represents the font color of the button when the mouse hover the button.
3.	Bd -->	It represents the border width in pixels.
4.	Bg -->	It represents the background color of the button.
5.	Command -->	It is set to the function call which is scheduled when the function is called.
6.	Fg -->	Foreground color of the button.
7.	Font -->	The font of the button text.
8.	Height -->	The height of the button. The height is represented in the number of text lines for the textual lines or the number of pixels for the images.
9.	Highlightcolor -->	The color of the highlight when the button has the focus.
10.	Image -->	It is set to the image displayed on the button.
11.	justify -->	It illustrates the way by which the multiple text lines are represented. It is set to LEFT for left justification, RIGHT for the right justification, and CENTER for the center.
12.	Padx -->	Additional padding to the button in the horizontal direction.
13.	pady -->	Additional padding to the button in the vertical direction.
14.	Relief -->	It represents the type of the border. It can be SUNKEN, RAISED, GROOVE, and RIDGE.
15.	State -->	This option is set to DISABLED to make the button unresponsive. The ACTIVE represents the active state of the button.
16.	Underline -->	Set this option to make the button text underlined.
17.	Width -->	The width of the button. It exists as a number of letters for textual buttons or pixels for image buttons.
18.	Wraplength -->	If the value is set to a positive number, the text lines will be wrapped to fit within this length.
'''

from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("400x125")
root.config(bg="sky blue")
root.resizable(0,0)

def RedButton():
    messagebox.showinfo("Red Color", "Red Button Clicked")
def GreenButton():
    messagebox.showinfo("Green Color", "Green Button Clicked")
def YellowButton():
    messagebox.showinfo("Yellow Color", "Yellow Button Clicked")
def BlueButton():
    messagebox.showinfo("Blue Color", "Blue Button Clicked")

b1 = Button(root, text="Red Button", command=RedButton, bd=2, relief=RIDGE, bg="sky blue", fg="red", activeforeground="black", activebackground="red", font=("Poor Richard", 16, "italic"),)
b1.pack(side=LEFT)

b2 = Button(root, text="Green Button", command=GreenButton, bd=2, relief=RIDGE, bg="sky blue", fg="green", activeforeground="black", activebackground="green", font=("Poor Richard", 16, "italic"),)
b2.pack(side=RIGHT)

b3 = Button(root, text="Yellow Button", command=YellowButton, bd=2, relief=RIDGE, bg="sky blue", fg="yellow", activeforeground="black", activebackground="yellow", font=("Poor Richard", 16, "italic"),)
b3.pack(side=TOP)

b4 = Button(root, text="Blue Button", command=BlueButton, bd=2, relief=RIDGE, bg="sky blue", fg="blue", activeforeground="black", activebackground="blue", font=("Poor Richard", 16, "italic"),)
b4.pack(side=BOTTOM)

root.mainloop()
