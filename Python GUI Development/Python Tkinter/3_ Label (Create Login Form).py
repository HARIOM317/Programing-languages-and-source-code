'''
The Label is used to specify the container box where we can place the text or images. This widget is used to provide the message to the user about other widgets used in the python application.
'''

# Creating a login form using labels
from tkinter import *
top = Tk()
top.geometry("400x250")
user_name = Label(top, text="Username").place(x=30, y=50)
password = Label(top, text="Password").place(x=30, y=90)

submit_button = Button(top, text="submit", activebackground="pink", activeforeground="blue").place(x=30, y=120)

e1 = Entry(top, width=20).place(x=100, y=50)
e2 = Entry(top, width=20).place(x=100, y=90)

top.mainloop()
