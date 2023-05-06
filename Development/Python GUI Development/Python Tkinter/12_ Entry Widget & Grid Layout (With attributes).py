'''
The entry widget is used to display the single-line text field to the user. It is commonly used to accept user values.

A list of possible options is given below.

SN	Option	Description
___________________________________________________________________________________________________________

1.	bg -->	The background color of the widget.
2.	bd -->	The border width of the widget in pixels.
3.	cursor -->	The mouse pointer will be changed to the cursor type set to the arrow, dot, etc.
4.	exportselection -->	The text written inside the entry box will be automatically copied to the clipboard by default. We can set the exportselection to 0 to not copy this.
5.	fg -->	It represents the color of the text.
6.	font -->	It represents the font type of the text.
7.	highlightbackground -->	It represents the color to display in the traversal highlight region when the widget does not have the input focus.
8.	highlightcolor -->	It represents the color to use for the traversal highlight rectangle that is drawn around the widget when it has the input focus.
9.	highlightthickness -->	It represents a non-negative value indicating the width of the highlight rectangle to draw around the outside of the widget when it has the input focus.
10.	insertbackground -->	It represents the color to use as background in the area covered by the insertion cursor. This color will normally override either the normal background for the widget.
11.	insertborderwidth -->	It represents a non-negative value indicating the width of the 3-D border to draw around the insertion cursor. The value may have any of the forms acceptable to Tk_GetPixels.
12.	insertofftime -->	It represents a non-negative integer value indicating the number of milliseconds the insertion cursor should remain "off" in each blink cycle. If this option is zero, then the cursor doesn't blink: it is on all the time.
13.	insertontime -->	Specifies a non-negative integer value indicating the number of milliseconds the insertion cursor should remain "on" in each blink cycle.
14.	insertwidth -->	It represents the value indicating the total width of the insertion cursor. The value may have any of the forms acceptable to Tk_GetPixels.
15.	justify -->	It specifies how the text is organized if the text contains multiple lines.
16.	relief -->	It specifies the type of the border. Its default value is FLAT.
17.	selectbackground -->	The background color of the selected text.
18.	selectborderwidth -->	The width of the border to display around the selected task.
19.	selectforeground -->	The font color of the selected task.
20.	show -->	It is used to show the entry text of some other type instead of the string. For example, the password is typed using stars (*).
21.	textvariable -->	It is set to the instance of the StringVar to retrieve the text from the entry.
22.	width -->	The width of the displayed text or image.
23.	xscrollcommand -->	The entry widget can be linked to the horizontal scrollbar if we want the user to enter more text then the actual width of the widget.
'''
from tkinter import *
root = Tk()
root.geometry("400x275")
root.config(bg="#AEC6CF")
root.resizable(0,0)

def getvals():
    pass

first_name = Label(root, text="First Name", fg="black", bg="#AEC6CF", font=("Aparajita", 16))
last_name = Label(root, text="Last Name", fg="black", bg="#AEC6CF", font=("Aparajita", 16))
age = Label(root, text="Age", fg="black", bg="#AEC6CF", font=("Aparajita", 16))
gender = Label(root, text="Gender", fg="black", bg="#AEC6CF", font=("Aparajita", 16))
email = Label(root, text="Email", fg="black", bg="#AEC6CF", font=("Aparajita", 16))
create_password = Label(root, text="Create Password", fg="black", bg="#AEC6CF", font=("Aparajita", 16))
confirm_password = Label(root, text="Confirm Password", fg="black", bg="#AEC6CF", font=("Aparajita", 16))

first_name.grid()
last_name.grid()
age.grid()
gender.grid()
email.grid()
create_password.grid()
confirm_password.grid()

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
f_name_value = StringVar()
l_name_value = StringVar()
age_value = IntVar()
gender_value = StringVar()
email_value = StringVar()
create_password = StringVar()
confirm_password = StringVar()

f_entry = Entry(root, textvariable=f_name_value, bg="light blue", fg="dark blue", font="Aparajita 14", exportselection=0, insertbackground="red", insertborderwidth=2, selectbackground="yellow", selectforeground="red")

l_entry = Entry(root, textvariable=l_name_value, bg="light blue", fg="dark blue", font="Aparajita 14", exportselection=0, insertbackground="red", insertborderwidth=2, selectbackground="yellow", selectforeground="red")

age_entry = Entry(root, textvariable=age_value, bg="light blue", fg="dark blue", font="Aparajita 14", exportselection=0, insertbackground="red", insertborderwidth=2, selectbackground="yellow", selectforeground="red")

gender_entry = Entry(root, textvariable=gender_value, bg="light blue", fg="dark blue", font="Aparajita 14", exportselection=0, insertbackground="red", insertborderwidth=2, selectbackground="yellow", selectforeground="red")

email_entry = Entry(root, textvariable=email_value, bg="light blue", fg="dark blue", font="Aparajita 14", exportselection=0, insertbackground="red", insertborderwidth=2, selectbackground="yellow", selectforeground="red")

password_entry = Entry(root, textvariable=create_password, bg="light blue", fg="dark blue", font="Aparajita 14", exportselection=0, insertbackground="red",show="*" ,insertborderwidth=2, selectbackground="yellow", selectforeground="red")

password_entry_again = Entry(root, textvariable=confirm_password, bg="light blue", fg="dark blue", font="Aparajita 14", exportselection=0, insertbackground="red",show="*" ,insertborderwidth=2, selectbackground="yellow", selectforeground="red")

f_entry.grid(row=0, column=1)
l_entry.grid(row=1, column=1)
age_entry.grid(row=2, column=1)
gender_entry.grid(row=3, column=1)
email_entry.grid(row=4, column=1)
password_entry.grid(row=5, column=1)
password_entry_again.grid(row=6, column=1)

Button(text="Submit", command=getvals, bg="sky blue", fg="red", font=("Poor Richard", 16)).grid(row=7, column=1)

root.mainloop()
