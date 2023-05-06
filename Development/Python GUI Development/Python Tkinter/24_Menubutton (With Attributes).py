'''
TODO: The Menubutton is used to implement various types of menus in the python application. A Menu is associated with the Menubutton that can display the choices of the Menubutton when clicked by the user.

A list of various options is given below.

SN	Option	Description
---------------------------------------------------------------------------------------------------------------
1.	activebackground -->	The background color of the widget when the widget is under focus.
2.	activeforeground -->	The font color of the widget text when the widget is under focus.
3.	anchor -->	It specifies the exact position of the widget content when the widget is assigned more space than needed.
4.	bg -->	It specifies the background color of the widget.
5.	bitmap -->	It is set to the graphical content which is to be displayed to the widget.
6.	bd -->	It represents the size of the border. The default value is 2 pixels.
7.	cursor -->	The mouse pointer will be changed to the cursor type specified when the widget is under the focus. The possible value of the cursor type is arrow, or dot etc.
8.	direction -->	It direction can be specified so that menu can be displayed to the specified direction of the button. Use LEFT, RIGHT, or ABOVE to place the widget accordingly.
9.	disabledforeground -->	The text color of the widget when the widget is disabled.
10.	fg -->	The normal foreground color of the widget.
11.	height -->	The vertical dimension of the Menubutton. It is specified as the number of lines.
12.	highlightcolor -->	The highlight color shown to the widget under focus.
13.	image -->	The image displayed on the widget.
14.	justify -->	This specified the exact position of the text under the widget when the text is unable to fill the width of the widget. We can use the LEFT for the left justification, RIGHT for the right justification, CENTER for the centre justification.
15.	menu -->	It represents the menu specified with the Menubutton.
16.	padx -->	The horizontal padding of the widget.
17.	pady -->	The vertical padding of the widget.
18.	relief -->	This option specifies the type of the border. The default value is RAISED. It can be SUNKEN, RAISED, GROOVE, and RIDGE.
19.	state -->	The normal state of the Mousebutton is enabled. We can set it to DISABLED to make it unresponsive.
20.	text -->	The text shown with the widget.
21.	textvariable -->	We can set the control variable of string type to the text variable so that we can control the text of the widget at runtime.
22.	underline -->	The text of the widget is not underlined by default but we can set this option to make the text of the widget underlined.
23.	width -->	It represents the width of the widget in characters. The default value is 20.
24.	wraplength -->	We can break the text of the widget in the number of lines so that the text contains the number of lines not greater than the specified value.
'''

from tkinter import *
root = Tk()
root.geometry('200x250')

menubutton = Menubutton(root, text="Language", activebackground="Yellow", relief=GROOVE, activeforeground="Red", bd=3, bg="sky blue", fg="blue", width=20)
menubutton.grid()

menubutton.menu = Menu(menubutton)
menubutton["menu"] = menubutton.menu

menubutton.menu.add_checkbutton(label="Hindi", variable=IntVar)
menubutton.menu.add_checkbutton(label="English", variable=IntVar)
menubutton.pack()


root.mainloop()
