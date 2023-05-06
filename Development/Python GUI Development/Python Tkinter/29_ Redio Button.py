'''
Todo ==> The Radiobutton widget is used to implement one-of-many selection in the python application. It shows multiple choices to the user out of which, the user can select only one out of them. We can associate different methods with each of the radiobutton.
'''

from tkinter import *
from tkinter import messagebox

def fev_lang():
    messagebox.showinfo(f"Favorite Language", f"Your Favorite Language is {languages[var.get()]}.")

root = Tk()
root.geometry("400x400")

var = IntVar()
var.set(1)

Label(root, text="Which is your favorite language?", justify=LEFT, padx=15, font="lucida 16 bold").pack()

languages = ['C++', 'Java', 'Python', 'Java Script', 'Other', 'None']
for i in range(len(languages)):
    radio = Radiobutton(root, text=languages[i], padx=15, variable=var, value=i).pack(anchor='w')

Button(root, text="Confirm",command=fev_lang).pack()
root.mainloop()
