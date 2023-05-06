'''
Todo: The scrollbar widget is used to scroll down the content of the other widgets like listbox, text, and canvas. However, we can also create the horizontal scrollbars to the Entry widget.

A list of possible options is given below.

SN	Option	Description
------------------------------------------------------------------------------------------------------------------
1.	activebackground --> 	The background color of the widget when it has the focus.
2.	bg --> 	The background color of the widget.
3.	bd --> 	The border width of the widget.
4.	command --> 	It can be set to the procedure associated with the list which can be called each time when the scrollbar is moved.
5.	cursor --> 	The mouse pointer is changed to the cursor type set to this option which can be an arrow, dot, etc.
6.	elementborderwidth --> 	It represents the border width around the arrow heads and slider. The default value is -1.
7.	Highlightbackground --> 	The focus highlighcolor when the widget doesn't have the focus.
8.	highlighcolor --> 	The focus highlighcolor when the widget has the focus.
9.	highlightthickness --> 	It represents the thickness of the focus highlight.
10.	jump --> 	It is used to control the behavior of the scroll jump. If it set to 1, then the callback is called when the user releases the mouse button.
11.	orient --> 	It can be set to HORIZONTAL or VERTICAL depending upon the orientation of the scrollbar.
12.	repeatdelay --> 	This option tells the duration up to which the button is to be pressed before the slider starts moving in that direction repeatedly. The default is 300 ms.
13.	repeatinterval --> 	The default value of the repeat interval is 100.
14.	takefocus --> 	We can tab the focus through this widget by default. We can set this option to 0 if we don't want this behavior.
15.	troughcolor --> 	It represents the color of the trough.
16.	width --> 	It represents the width of the scrollbar.
===================================================================================================================

Methods: The widget provides the following methods.

SN	Method	Description
------------------------------------------------------------------------------------------------------------------
1.	get() --> 	It returns the two numbers a and b which represents the current position of the scrollbar.
2.	set(first, last) --> 	It is used to connect the scrollbar to the other widget w. The yscrollcommand or xscrollcommand of the other widget to this method.
'''

from tkinter import *

root = Tk()
root.geometry('800x500')

''' 
For connecting a scrollbar to a widget
Condition 1: widget(yscrollcommand = scrollbar.set)
Condition 2: scrollbar.config(command=widget.yview)
'''

scrollbar1 = Scrollbar(root, bd=3, bg="red", width=25)
scrollbar1.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand=scrollbar1.set, font=("Poor Richard", 12))
for i in range(1, 1001):
    listbox.insert(END, f"Item {i}")

listbox.pack(fill=BOTH, padx=20, pady=50)
scrollbar1.config(command=listbox.yview)
#_______________________________________________________________________

scrollbar2 = Scrollbar(root, bd=5, width=25)
scrollbar2.pack(side=RIGHT, fill=Y)

text = Text(root, yscrollcommand=scrollbar2.set)
text.pack(fill=BOTH, padx=20, pady=20)
scrollbar2.config(command=text.yview)

root.mainloop()