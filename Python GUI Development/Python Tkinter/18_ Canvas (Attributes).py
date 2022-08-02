'''
A list of possible options is given below.

SN	Option	Description
--------------------------------------------------------------------------------------------------------------
1.	bd -->	The represents the border width. The default width is 2.
2.	bg -->	It represents the background color of the canvas.
3.	confine -->	It is set to make the canvas unscrollable outside the scroll region.
4.	cursor -->	The cursor is used as the arrow, circle, dot, etc. on the canvas.
5.	height -->	It represents the size of the canvas in the vertical direction.
6.	highlightcolor -->	It represents the highlight color when the widget is focused.
7.	relief -->	It represents the type of the border. The possible values are SUNKEN, RAISED, GROOVE, and RIDGE.
8.	scrollregion -->	It represents the coordinates specified as the tuple containing the area of the canvas.
9.	width -->	It represents the width of the canvas.
10.	xscrollincrement -->	If it is set to a positive value. The canvas is placed only to the multiple of this value.
11.	xscrollcommand -->	If the canvas is scrollable, this attribute should be the .set() method of the horizontal scrollbar.
12.	yscrollincrement -->	Works like xscrollincrement, but governs vertical movement.
13.	yscrollcommand -->	If the canvas is scrollable, this attribute should be the .set() method of the vertical scrollbar.
'''

from tkinter import *
root =Tk()
root.geometry('200x200')

# Creating a canvas
c = Canvas(root, height=200, width=200, bg='pink', bd=5, cursor='plus')
arc = c.create_arc((5, 10, 150, 200), start=0, extent=150, fill="white")
c.pack()

root.mainloop()