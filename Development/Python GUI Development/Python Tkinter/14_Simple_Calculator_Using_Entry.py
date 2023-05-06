from tkinter import *
from functools import partial

def callResult(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1) + int(num2)
    label_result.config(text="Result = %d" %result)
    return

root = Tk()
root.config(background="light blue")
root.geometry('250x150')
root.title("Calculator")

number1 = StringVar()
number2 = StringVar()
labelNum1 = Label(root, text="First Number", bg="light blue").grid(row=2, column=0, sticky='w')
labelNum2 = Label(root, text="Second Number", bg="light blue").grid(row=3, column=0, sticky='w')

label_Result = Label(root, bg="light blue")
label_Result.grid(row=8, column=1)

entryNum1 = Entry(root, textvariable=number1).grid(row=2, column=1)
entryNum2 = Entry(root, textvariable=number2).grid(row=3, column=1)

callResult = partial(callResult, label_Result, number1, number2)
button = Button(root, text="Calculate", command=callResult, bg="sky blue").grid(row=4, column=0)


root.mainloop()


