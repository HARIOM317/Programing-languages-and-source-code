'''
A list of possible options is given below.

SN	Option	Description
----------------------------------------------------------------------------------------------------------
1.	bg -->	The background color of the widget.
2.	bd -->	It represents the size of the border. Default value is 2 pixel.
3.	cursor -->	The mouse pointer will look like the cursor type like dot, arrow, etc.
4.	font -->	The font type of the Listbox items.
5.	fg -->	The color of the text.
6.	height -->	It represents the count of the lines shown in the Listbox. The default value is 10.
7.	highlightcolor -->	The color of the Listbox items when the widget is under focus.
8.	highlightthickness -->	The thickness of the highlight.
9.	relief -->	The type of the border. The default is SUNKEN.
10.	selectbackground -->	The background color that is used to display the selected text.
11.	selectmode -->	It is used to determine the number of items that can be selected from the list. It can set to BROWSE, SINGLE, MULTIPLE, EXTENDED.
12.	width -->	It represents the width of the widget in characters.
13.	xscrollcommand -->	It is used to let the user scroll the Listbox horizontally.
14.	yscrollcommand -->  It is used to let the user scroll the Listbox vertically.
==================================================================================================================

Methods: There are the following methods associated with the Listbox.

SN	Method	Description
----------------------------------------------------------------------------------------------------------
1.	activate(index) -->	It is used to select the lines at the specified index.
2.	curselection() -->	It returns a tuple containing the line numbers of the selected element or elements, counting from 0. If nothing is selected, returns an empty tuple.
3.	delete(first, last = None) -->	It is used to delete the lines which exist in the given range.
4.	get(first, last = None) -->	It is used to get the list items that exist in the given range.
5.	index(i) -->	It is used to place the line with the specified index at the top of the widget.
6.	insert(index, *elements) -->	It is used to insert the new lines with the specified number of elements before the specified index.
7.	nearest(y) -->	It returns the index of the nearest line to the y coordinate of the Listbox widget.
8.	see(index) -->	It is used to adjust the position of the listbox to make the lines specified by the index visible.
9.	size() -->	It returns the number of lines that are present in the Listbox widget.
10.	xview() -->	This is used to make the widget horizontally scrollable.
11.	xview_moveto(fraction) -->	It is used to make the listbox horizontally scrollable by the fraction of width of the longest line present in the listbox.
12.	xview_scroll(number, what) -->	It is used to make the listbox horizontally scrollable by the number of characters specified.
13.	yview() -->	It allows the Listbox to be vertically scrollable.
14.	yview_moveto(fraction) -->	It is used to make the listbox vertically scrollable by the fraction of width of the longest line present in the listbox.
15.	yview_scroll (number, what) -->	It is used to make the listbox vertically scrollable by the number of characters specified.
'''

from tkinter import *

root = Tk()
root.geometry('300x400')

label = Label(root, text="A list of various countries:", font=("Poor Richard", 15))
listbox = Listbox(root, bg="light blue", bd=0, relief=FLAT, fg="blue", height=10, width=30, selectforeground="Red", selectbackground="Yellow", selectborderwidth=30, selectmode=BROWSE, font="Georgia 16 italic")
listbox.insert(1, "India")
listbox.insert(2, "Japan")
listbox.insert(3, "USA")
listbox.insert(4, "England")
listbox.insert(5, "Australiya")
listbox.insert(6, "Fransh")

listbox.xview()

Delete_Button = Button(root, text="Delete Item", command=lambda listbox=listbox: listbox.delete(ANCHOR), pady=10, padx=10, bg="sky blue", font="Georgia 16")

label.pack()
listbox.pack()
Delete_Button.pack()

root.mainloop()