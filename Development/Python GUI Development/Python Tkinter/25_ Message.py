'''
TODO: The Message widget is used to show the message to the user regarding the behaviour of the python application. The message widget shows the text messages to the user which can not be edited

A list of possible options is given below.

SN	Option	Description
-----------------------------------------------------------------------------------------------------------------
1.	anchor -->	It is used to decide the exact position of the text within the space provided to the widget if the widget contains more space than the need of the text. The default is CENTER.
2.	bg -->	The background color of the widget.
3.	bitmap -->	It is used to display the graphics on the widget. It can be set to any graphical or image object.
4.	bd -->	It represents the size of the border in the pixel. The default size is 2 pixel.
5.	cursor -->	The mouse pointer is changed to the specified cursor type. The cursor type can be an arrow, dot, etc.
6.	font -->	The font type of the widget text.
7.	fg -->	The font color of the widget text.
8.	height -->	The vertical dimension of the message.
9.	image -->	We can set this option to a static image to show that onto the widget.
10.	justify -->	This option is used to specify the alignment of multiple line of code with respect to each other. The possible values can be LEFT (left alignment), CENTER (default), and RIGHT (right alignment).
11.	padx -->	The horizontal padding of the widget.
12.	pady -->	The vertical padding of the widget.
13.	relief -->	It represents the type of the border. The default type is FLAT.
14.	text -->	We can set this option to the string so that the widget can represent the specified text.
15.	textvariable -->	This is used to control the text represented by the widget. The textvariable can be set to the text that is shown in the widget.
16.	underline -->	The default value of this option is -1 that represents no underline. We can set this option to an existing number to specify that nth letter of the string will be underlined.
17.	width -->	It specifies the horizontal dimension of the widget in the number of characters (not pixel).
18.	wraplength -->	We can wrap the text to the number of lines by setting this option to the desired number so that each line contains only that number of characters.
'''

from tkinter import *
root = Tk()
root.geometry('400x300')
var = StringVar()
msg = Message(root, text="Hello, My name is Hariom Singh Rajput.", width=225, anchor='e', bg='yellow', fg='Red', font=("Poor Richard", 20), padx=20, pady=20, bd=5, relief=RIDGE, cursor='plus')
msg.pack()

root.mainloop()
