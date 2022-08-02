# The Checkbutton is used to display the CheckButton on the window.
from tkinter import *

def getvals():
    print("Submission competed!")
    print(f'''
__________ The Form of Our new Customer __________
Name :  {nameValue.get()}, 
Mobile number :  {MobileValue.get()},
Gender :  {GenderValue.get()},
Emergency Number :  {EmergencyValue.get()},
Payment Method :  {paymentValue.get()},
Food service :  {FoodServiceValue.get()}
\n''')

    with open("15_Travel Record.txt", 'a') as f:
        f.write(f'''
__________ The Form of Our new Customer __________
Name :  {nameValue.get()}, 
Mobile number :  {MobileValue.get()},
Gender :  {GenderValue.get()},
Emergency Number :  {EmergencyValue.get()},
Payment Method :  {paymentValue.get()},
Food service :  {FoodServiceValue.get()}
\n''')

root = Tk()
root.geometry('450x250')
root.resizable(0,0)

# Heading
Label(root, text="Wellcome to HSR travels", font="comicsansms 15 bold", pady=10).grid(row=1, column=3)

# Text for our form
name = Label(root, text="Name")
Mobile = Label(root, text="Mobile")
Gender = Label(root, text="Gender")
Emergency = Label(root, text="Emergency Number")
payment = Label(root, text="Payment Mode")

# Pack texts in our form
name.grid(row=2, column=2)
Mobile.grid(row=3, column=2)
Gender.grid(row=4, column=2)
Emergency.grid(row=5, column=2)
payment.grid(row=6, column=2)

# tkinter variables for storing entries
nameValue = StringVar()
MobileValue = StringVar()
GenderValue = StringVar()
EmergencyValue = StringVar()
paymentValue = StringVar()
FoodServiceValue = IntVar()

# Entries for our form
nameEntry = Entry(root, textvariable=nameValue)
MobileEntry = Entry(root, textvariable=MobileValue)
GenderEntry = Entry(root, textvariable=GenderValue)
EmergencyEntry = Entry(root, textvariable=EmergencyValue)
paymentEntry = Entry(root, textvariable=paymentValue)

# Packing the entries
nameEntry.grid(row=2, column=3)
MobileEntry.grid(row=3, column=3)
GenderEntry.grid(row=4, column=3)
EmergencyEntry.grid(row=5, column=3)
paymentEntry.grid(row=6, column=3)

# Add a checkbox and packing it
foodService = Checkbutton(text="want to prebook your meals?", variable=FoodServiceValue)
foodService.grid(row=7, column=3)

# create a button and packing it and also assigning it a command
Button(text="Submit", command=getvals).grid(row=8, column=3)

root.mainloop()
