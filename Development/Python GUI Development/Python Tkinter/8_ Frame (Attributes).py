'''
A list of possible options is given below.

SN	Option	Description
1	bd -->	It represents the border width.
2	bg -->	The background color of the widget.
3	cursor -->	The mouse pointer is changed to the cursor type set to different values like an arrow, dot, etc.
4	height -->	The height of the frame.
5	highlightbackground -->	The color of the background color when it is under focus.
6	highlightcolor -->	The text color when the widget is under focus.
7	highlightthickness -->	It specifies the thickness around the border when the widget is under the focus.
8	relief -->	It specifies the type of the border. The default value if FLAT.
9	width -->	It represents the width of the widget.
'''

from tkinter import *
root = Tk()
root.geometry('888x470')
root.resizable(0,0)

f1 = Frame(root, bg="orange", borderwidth=2, relief=SUNKEN)
f1.pack(side=TOP, fill=X)

f2 = Frame(root, bg="light blue", bd=3, relief=SUNKEN, cursor="plus")
f2.pack(side=LEFT, fill=Y, pady=35)

f3 = Frame(root, bg="light blue", borderwidth=3, relief=SUNKEN, cursor='plus')
f3.pack(side=RIGHT, fill=Y, pady=35)

l1 = Label(f1, text="Wellcome to my code editor", bg="orange", fg='black', font="Aparajita 15 italic")
l1.pack()

l2 = Label(f2, text="Your Python Projects", bg="sky blue", fg='black', font="Aparajita 16 italic")
l2.pack()

l3 = Label(f3, text="Your Python History", bg="sky blue", fg='black', font="Aparajita 16 italic")
l3.pack()

# Add entry form for writing something by single line.
working_area = Text(root, width=70).place(x=165, y=50)

root.mainloop()
