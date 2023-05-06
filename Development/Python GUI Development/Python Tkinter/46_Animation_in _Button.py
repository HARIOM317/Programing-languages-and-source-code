from tkinter import *
root = Tk()
root.geometry('400x400')

# Define some variables
count = 0
size = 25

# Contract the button
def contract():
    global count, size
    if count <= 10 and count > 0:
        size -= 2
        # Configure button font size
        my_button.config(font=("Georgia", size))
        # Change button position (You can also remove this if you don't want to change the button position)
        my_button.pack_configure(pady=size)
        count -= 2
        # Set the timer
        root.after(10, contract)    # 10 ms = 0.01 s


# Expand the button
def expand():
    global count, size
    if count < 10:
        size += 2
        # Configure button font size
        my_button.config(font=("Georgia", size))
        # Change button position
        my_button.pack_configure(pady=size)

        count += 2
        # Set the timer
        root.after(10, expand)    # 10 ms = 0.01 s
    elif count == 10:
        contract()




# create a button
my_button = Button(root, text='Click me!', font=("Georgia", 25), command=expand, fg='red', bd=0, activeforeground='red')
my_button.pack(pady=100)

root.mainloop()