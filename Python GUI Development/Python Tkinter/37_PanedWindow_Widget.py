'''
todo: The PanedWindow widget acts like a Container widget which contains one or more child widgets (panes) arranged horizontally or vertically. The child panes can be resized by the user, by moving the separator lines known as sashes by using the mouse. Each pane contains only one widget. The PanedWindow is used to implement the different layouts in the python applications.

A list of possible options is given below.

SN	Option	    Description
1.	bg -->	It represents the background color of the widget when it doesn't have the focus.
2.	bd -->	It represents the 3D border size of the widget. The default option specifies that the trough contains no border whereas the arrowheads and slider contain the 2-pixel border size.
3.	borderwidth -->	It represents the border width of the widget. The default is 2 pixel.
4.	cursor -->	The mouse pointer is changed to the specified cursor type when it is over the window.
5.	handlepad -->	This option represents the distance between the handle and the end of the sash. For the horizontal orientation, it is the distance between the top of the sash and the handle. The default is 8 pixels.
6.	handlesize -->	It represents the size of the handle. The default size is 8 pixels. However, the handle will always be a square.
7.	height -->	It represents the height of the widget. If we do not specify the height, it will be calculated by the height of the child window.
8. orient -->  The orient will be set to HORIZONTAL if we want to place the child windows side by side. It can be set to VERTICAL if we want to place the child windows from top to bottom.
9.	relief -->	 It represents the type of the border. The default is FLAT.
10.	sashpad -->   It represents the padding to be done around each sash. The default is 0.
11.	sashrelief -->	It represents the type of the border around each of the sash. The default is FLAT.
12.	sashwidth -->	It represents the width of the sash. The default is 2 pixels.
13.	showhandle -->	It is set to True to display the handles. The default value is false.
14.	Width -->	It represents the width of the widget. If we don't specify the width of the widget, it will be calculated by the size of the child widgets.
Todo: ********************************************************************************************************

Methods:  There are the following methods that are associated with the PanedWindow.

SN	Method	                            Description
1.	add(child, options) -->	It is used to add a window to the parent window.
2.	get(startindex, endindex) -->	This method is used to get the text present at the specified range.
3.	config(options) -->	It is used to configure the widget with the specified options.
'''

from tkinter import *
root = Tk()
root.geometry('600x150')

def sum():
    a = int(e1.get())
    b = int(e2.get())
    ans = str(a+b)
    left.insert(1, ans)

w1 = PanedWindow(root, bg='light blue')
w1.pack(fill=BOTH, expand=True)

left =Entry(w1, borderwidth=5, bg='yellow', width=50)
w1.add(left)

w2 = PanedWindow(w1, orient=VERTICAL, bg='light green')
w1.add(w2)

e1 = Entry(w2, bg='light pink')
e2 = Entry(w2, bg='light pink')

w2.add(e1)
w2.add(e2)

button = Button(w1, text='Sum', command=sum, borderwidth=3, relief=SUNKEN, bg='orange')
w2.add(button)


root.mainloop()