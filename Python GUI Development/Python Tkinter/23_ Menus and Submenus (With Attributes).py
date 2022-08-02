'''
A list of possible options is given below.

SN	Option	Description
------------------------------------------------------------------------------------------------------------------
1.	activebackground -->	The background color of the widget when the widget is under the focus.
2.	activeborderwidth -->	The width of the border of the widget when it is under the mouse. The default is 1 pixel.
3.	activeforeground -->	The font color of the widget when the widget has the focus.
4.	bg -->	The background color of the widget.
5.	bd -->	The border width of the widget.
6.	cursor -->	The mouse pointer is changed to the cursor type when it hovers the widget. The cursor type can be set to arrow or dot.
7.	disabledforeground -->	The font color of the widget when it is disabled.
8.	font -->	The font type of the text of the widget.
9.	fg -->	The foreground color of the widget.
10.	postcommand -->	The postcommand can be set to any of the function which is called when the mourse hovers the menu.
11.	relief -->	The type of the border of the widget. The default type is RAISED.
12.	image -->	It is used to display an image on the menu.
13.	selectcolor -->	The color used to display the checkbutton or radiobutton when they are selected.
14.	tearoff -->	By default, the choices in the menu start taking place from position 1. If we set the tearoff = 1, then it will start taking place from 0th position.
15.	title -->	Set this option to the title of the window if you want to change the title of the window.
===================================================================================================================

Methods:
        The Menu widget contains the following methods.

SN	Option	Description
------------------------------------------------------------------------------------------------------------------
1.	add_command(options) -->	It is used to add the Menu items to the menu.
2.	add_radiobutton(options) -->	This method adds the radiobutton to the menu.
3.	add_checkbutton(options) -->	This method is used to add the checkbuttons to the menu.
4.	add_cascade(options) -->	It is used to create a hierarchical menu to the parent menu by associating the given menu to the parent menu.
5.	add_seperator() -->	It is used to add the seperator line to the menu.
6.	add(type, options) -->	It is used to add the specific menu item to the menu.
7.	delete(startindex, endindex) -->	It is used to delete the menu items exist in the specified range.
8.	entryconfig(index, options) -->	It is used to configure a menu item identified by the given index.
9.	index(item) -->	It is used to get the index of the specified menu item.
10.	insert_seperator(index) -->	It is used to insert a seperator at the specified index.
11.	invoke(index) -->	It is used to invoke the associated with the choice given at the specified index.
12.	type(index) -->	It is used to get the type of the choice specified by the index.
'''

from tkinter import *

root = Tk()
root.geometry("824x412")
def myfunc():
    print("This is a function!")

MyMenuBar = Menu(root)

m1 = Menu(MyMenuBar, tearoff=0, activeforeground='red', activebackground='yellow', bg='light blue', fg='dark blue')
m1.add_command(label="create project", command=myfunc)
m1.add_command(label="new file", command=myfunc)
m1.add_command(label="open", command=myfunc)
m1.add_separator()
m1.add_command(label="save", command=myfunc)
m1.add_command(label="save all", command=myfunc)
m1.add_command(label="save as", command=myfunc)
m1.add_separator()
m1.add_command(label="close project", command=myfunc)
m1.add_command(label="print", command=myfunc)
m1.add_command(label="Export", command=myfunc)
m1.add_command(label="exit", command=myfunc)
root.config(menu=MyMenuBar)

MyMenuBar.add_cascade(label="File", menu=m1)

m2 = Menu(MyMenuBar, tearoff=0, activeforeground='red', activebackground='yellow', bg='light blue', fg='dark blue')
m2.add_command(label="cut", command=myfunc)
m2.add_command(label="copy", command=myfunc)
m2.add_command(label="paste", command=myfunc)
m2.add_separator()
m2.add_command(label="find", command=myfunc)
m2.add_command(label="replace", command=myfunc)
m2.add_command(label="select all", command=myfunc)
m2.add_separator()
m2.add_command(label="undo", command=myfunc)
m2.add_command(label="redo", command=myfunc)
m2.add_command(label="macros", command=myfunc)
root.config(menu=MyMenuBar)

MyMenuBar.add_cascade(label="Edit", menu=m2)

m3 = Menu(MyMenuBar, tearoff=0, activeforeground='red', activebackground='yellow', bg='light blue', fg='dark blue')
m3.add_command(label="Help", command=myfunc)
m3.add_command(label="Getting started", command=myfunc)
m3.add_command(label="about", command=myfunc)
m3.add_separator()
m3.add_command(label="tips", command=myfunc)
m3.add_command(label="content support", command=myfunc)
m3.insert_separator(5)
root.config(menu=MyMenuBar)

MyMenuBar.add_cascade(label="Help", menu=m3)

root.mainloop()
