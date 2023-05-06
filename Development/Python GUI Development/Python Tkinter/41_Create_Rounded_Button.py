from tkinter import *
root = Tk()
root.geometry('400x400')

def thing():
    my_label.config(text="You click me")

round_button = PhotoImage(file="A:\\Python GUI Development\\Python Tkinter\\Required Images\\rounded.png")

my_Button = Button(root, image=round_button, command=thing, relief=FLAT, bd=0)
my_Button.pack(pady=20)

my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()