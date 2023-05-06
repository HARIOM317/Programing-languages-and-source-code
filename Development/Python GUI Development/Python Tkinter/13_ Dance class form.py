from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x250")
root.resizable(0,0)
root.config(bg="#AEC6CF")

def ButtonMessage():
    messagebox.showinfo("Dance Class Acadmy", "Your form filled successfully!")

header = Label(text="Dance Class Form", bg="sky blue", fg="black", font=("Poor Richard", 18))
header.pack(side=TOP, fill=X)

first_name = Label(root, text="First Name", fg="black", bg="#AEC6CF", font=("Aparajita", 16))
last_name = Label(root, text="Last Name", fg="black", bg="#AEC6CF", font=("Aparajita", 16))
age = Label(root, text="Age", fg="black", bg="#AEC6CF", font=("Aparajita", 16))
gender = Label(root, text="Gender", fg="black", bg="#AEC6CF", font=("Aparajita", 16))
email = Label(root, text="Email", fg="black", bg="#AEC6CF", font=("Aparajita", 16))

first_name.place(x=10, y=40)
last_name.place(x=10, y=70)
age.place(x=10, y=100)
gender.place(x=10, y=130)
email.place(x=10, y=160)

e1 = Entry(root, width=28, bg="#F5F5DC", font=("Georgia", 12)).place(x=100, y=45)
e2 = Entry(root, width=28, bg="#F5F5DC", font=("Georgia", 12)).place(x=100, y=75)
e3 = Entry(root, width=28, bg="#F5F5DC", font=("Georgia", 12)).place(x=100, y=105)
e4 = Entry(root, width=28, bg="#F5F5DC", font=("Georgia", 12)).place(x=100, y=135)
e5 = Entry(root, width=28, bg="#F5F5DC", font=("Georgia", 12)).place(x=100, y=165)

submit_button = Button(root, text="Submit", bg="light blue", activebackground="sky blue", activeforeground="red", font=("Poor Richard", 16), command=ButtonMessage).place(x=165, y=200)

root.mainloop()
