'''
Todo: The messagebox module is used to display the message boxes in the python applications. There are the various functions which are used to display the relevant messages depending upon the application requirements.

There is one of the following functions used to show the appropriate message boxes. All the functions are used with the same syntax but have the specific functionalities.

1. showinfo(): The showinfo() messagebox is used where we need to show some relevant information to the user.
2. showwarning(): This method is used to display the warning to the user.
3. showerror(): This method is used to display the error message to the user.
4. askquestion(): This method is used to ask some question to the user which can be answered in yes or no.
5. askokcancel(): This method is used to confirm the user's action regarding some application activity.
6. askyesno(): This method is used to ask the user about some action to which, the user can answer in yes or no.
7. askretrycancel(): This method is used to ask the user about doing a particular task again or not.
'''

from tkinter import *
from tkinter import messagebox

def Information():
    messagebox.showinfo("Information", "information")

def Warning():
    messagebox.showwarning("Warning", "warning")

def Error():
    messagebox.showerror("Error", "error")

def AskQuestion():
    question = messagebox.askquestion("Confirm", "Are you sure")
    if question == "yes":
        msg = "Thanks, Rate us now on Microsoft Store"
    else:
        msg = "Tell us what went wrong? We will call you soon."
    messagebox.showinfo("experience", msg)

def Askokcancel():
    messagebox.askokcancel("Redirect", "Redirecting you to www.google.com")

def Askyesno():
    messagebox.askyesno("Application", "Got it")

def Askyesnocancel():
    messagebox.askyesnocancel("Application", "Confirm")

def Askretrycancel():
    messagebox.askretrycancel("Application", "Retry")

root = Tk()
root.geometry('250x400')
root.config(bg="light blue")

Button(root, text="Information", bg="light blue", fg="Red", font=("Georgia", 16), command=Information).pack()
Button(root, text="Warning", bg="light blue", fg="Red", font=("Georgia", 16), command=Warning).pack()
Button(root, text="Error", bg="light blue", fg="Red", font=("Georgia", 16), command=Error).pack()
Button(root, text="Ask question", bg="light yellow", fg="Red", font=("Georgia", 16), command=AskQuestion).pack()
Button(root, text="Ask ok cancel", bg="light blue", fg="Red", font=("Georgia", 16), command=Askokcancel).pack()
Button(root, text="Ask yes no", bg="light blue", fg="Red", font=("Georgia", 16), command=Askyesno).pack()
Button(root, text="Ask yes no cancel", bg="light blue", fg="Red", font=("Georgia", 16), command=Askyesnocancel).pack()
Button(root, text="Ask retry cancel", bg="light blue", fg="Red", font=("Georgia", 16), command=Askretrycancel).pack()
root.mainloop()
