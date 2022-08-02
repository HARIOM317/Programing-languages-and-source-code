'''
A list of possible options is given below.

SN	Option	Description
------------------------------------------------------------------------------------------------------------------
1.	activebackground -->	The background color of the widget when it has the focus.
2.	bg -->	The background color of the widget.
3.	bd -->	The border size of the widget. The default is 2 pixel.
4.	command -->	It is set to the procedure which is called each time when we move the slider. If the slider is moved rapidly, the callback is done when it settles.
5.	cursor -->	The mouse pointer is changed to the cursor type assigned to this option. It can be an arrow, dot, etc.
6.	digits -->	If the control variable used to control the scale data is of string type, this option is used to specify the number of digits when the numeric scale is converted to a string.
7.	font -->	The font type of the widget text.
8.	fg -->	The foreground color of the text.
9.	from_ -->	It is used to represent one end of the widget range.
10.	highlightbackground -->	The highlight color when the widget doesn't have the focus.
11.	highlighcolor -->	The highlight color when the widget has the focus.
12.	label -->	This can be set to some text which can be shown as a label with the scale. It is shown in the top left corner if the scale is horizontal or the top right corner if the scale is vertical.
13.	length -->	It represents the length of the widget. It represents the X dimension if the scale is horizontal or y dimension if the scale is vertical.
14.	orient -->	It can be set to horizontal or vertical depending upon the type of the scale.
15.	relief -->	It represents the type of the border. The default is FLAT.
16.	repeatdelay -->	This option tells the duration up to which the button is to be pressed before the slider starts moving in that direction repeatedly. The default is 300 ms.
17.	resolution -->	It is set to the smallest change which is to be made to the scale value.
18.	showvalue -->	The value of the scale is shown in the text form by default. We can set this option to 0 to suppress the label.
19.	sliderlength -->	It represents the length of the slider window along the length of the scale. The default is 30 pixels. However, we can change it to the appropriate value.
20.	state -->	The scale widget is active by default. We can set this to DISABLED to make it unresponsive.
21.	takefocus -->	The focus cycles through the scale widgets by default. We can set this option to 0 if we don't want this to happen.
22.	tickinterval -->	The scale values are displayed on the multiple of the specified tick interval. The default value of the tickinterval is 0.
23.	to -->	It represents a float or integer value that specifies the other end of the range represented by the scale.
24.	troughcolor -->	It represents the color of the through.
25.	variable -->	It represents the control variable for the scale.
26.	width -->	It represents the width of the through part of the widget.
==================================================================================================================

Methods:
SN	Method	Description
------------------------------------------------------------------------------------------------------------------
1.	get() -->	It is used to get the current value of the scale.
2.	set(value) -->	It is used to set the value of the scale.
'''

from tkinter import *

def select():
    sel = "Value = " + str(v.get())
    label.config(text=sel)

root = Tk()
root.geometry("400x400")

v = DoubleVar()
scale = Scale(root, variable=v, from_=0, to=100, orient=HORIZONTAL, tickinterval=20, width=25, length=350, bg="sky blue", fg="dark red", activebackground="Yellow", label="Set a Value", font=("Aparajita", 16), bd=5, relief=GROOVE, resolution=5, sliderlength=20, troughcolor="pink", sliderrelief="groove")
scale.pack(anchor=CENTER)

btn = Button(root, text="Value", command=select)
btn.pack(anchor=CENTER)

label = Label(root)
label.pack()

root.mainloop()
