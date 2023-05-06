'''
A list of possible options is given below.

SN	Option	Description
1.	activebackground -->	It represents the background color when the checkbutton is under the cursor.
2.	activeforeground -->	It represents the foreground color of the checkbutton when the checkbutton is under the cursor.
3.	bg -->	The background color of the button.
4.	bitmap -->	It displays an image (monochrome) on the button.
5.	bd -->	The size of the border around the corner.
6.	command -->	It is associated with a function to be called when the state of the checkbutton is changed.
7.	cursor -->	The mouse pointer will be changed to the cursor name when it is over the checkbutton.
8.	disableforeground -->	It is the color which is used to represent the text of a disabled checkbutton.
9.	font -->	It represents the font of the checkbutton.
10.	fg -->	The foreground color (text color) of the checkbutton.
11.	height -->	It represents the height of the checkbutton (number of lines). The default height is 1.
12.	highlightcolor -->	The color of the focus highlight when the checkbutton is under focus.
13.	image -->	The image used to represent the checkbutton.
14.	justify -->	This specifies the justification of the text if the text contains multiple lines.
15.	offvalue -->	The associated control variable is set to 0 by default if the button is unchecked. We can change the state of an unchecked variable to some other one.
16.	onvalue -->	The associated control variable is set to 1 by default if the button is checked. We can change the state of the checked variable to some other one.
17.	padx -->	The horizontal padding of the checkbutton
18.	pady -->	The vertical padding of the checkbutton.
19.	relief -->	The type of the border of the checkbutton. By default, it is set to FLAT.
20.	selectcolor -->	The color of the checkbutton when it is set. By default, it is red.
21.	selectimage -->	The image is shown on the checkbutton when it is set.
22.	state -->	It represents the state of the checkbutton. By default, it is set to normal. We can change it to DISABLED to make the checkbutton unresponsive. The state of the checkbutton is ACTIVE when it is under focus.
23.	underline -->	It represents the index of the character in the text which is to be underlined. The indexing starts with zero in the text.
24.	variable -->	It represents the associated variable that tracks the state of the checkbutton.
25.	width -->	It represents the width of the checkbutton. It is represented in the number of characters that are represented in the form of texts.
26.	wraplength -->	If this option is set to an integer number, the text will be broken into the number of pieces.
_________________________________________________________________________________________________________________

Methods:
The methods that can be called with the Checkbuttons are described in the following table.

SN	Method	Description
1.	deselect() -->	It is called to turn off the checkbutton.
2.	flash() -->	    The checkbutton is flashed between the active and normal colors.
3.	invoke() -->	This will invoke the method associated with the checkbutton.
4.	select() -->	It is called to turn on the checkbutton.
5.	toggle() -->	It is used to toggle between the different Checkbuttons.
'''

from tkinter import *
root = Tk()
root.geometry('200x220')

checkVar1 = IntVar()
checkVar2 = IntVar()
checkVar3 = IntVar()
checkVar4 = IntVar()
checkVar5 = IntVar()

checkButton1 = Checkbutton(root, text="C", variable=checkVar1, onvalue=1, offvalue=0, height=2, width=10, activeforeground="red", activebackground="yellow", bd=5, bg="sky blue", fg="black", pady=1, padx=2)
checkButton2 = Checkbutton(root, text="C++", variable=checkVar2, onvalue=1, offvalue=0, height=2, width=10, activeforeground="red", activebackground="yellow", bd=5, bg="sky blue", fg="black", pady=1, padx=2)
checkButton3 = Checkbutton(root, text="Java", variable=checkVar3, onvalue=1, offvalue=0, height=2, width=10, activeforeground="red", activebackground="yellow", bd=5, bg="sky blue", fg="black", pady=1, padx=2)
checkButton4 = Checkbutton(root, text="Python", variable=checkVar4, onvalue=1, offvalue=0, height=2, width=10, activeforeground="red", activebackground="yellow", bd=5, bg="sky blue", fg="black", pady=1, padx=2)
checkButton5 = Checkbutton(root, text="Java script", variable=checkVar5, onvalue=1, offvalue=0, height=2, width=10, activeforeground="red", activebackground="yellow", bd=5, bg="sky blue", fg="black", pady=1, padx=2)

checkButton1.pack()
checkButton2.pack()
checkButton3.pack()
checkButton4.pack()
checkButton5.pack()

root.mainloop()
