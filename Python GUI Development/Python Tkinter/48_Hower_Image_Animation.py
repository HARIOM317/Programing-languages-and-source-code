from tkinter import *
root = Tk()
root.geometry('800x500')

def change_pic(e):
    my_pic = PhotoImage(file="A:\\Python GUI Development\\Python Tkinter\\Required Images\\1.png")
    my_button.config(image=my_pic)
    my_button.image = my_pic

def change_back(e):
    my_pic = PhotoImage(file="A:\\Python GUI Development\\Python Tkinter\\Required Images\\rounded.png")
    my_button.config(image=my_pic)
    my_button.image = my_pic

def do_something():
    my_label = Label(root, text="You clicked the button", font="Georgia 20 bold italic", fg='dark blue')
    my_label.pack(pady=20)


my_pic = PhotoImage(file="A:\\Python GUI Development\\Python Tkinter\\Required Images\\rounded.png")

my_button = Button(root, image=my_pic, command=do_something)
my_button.pack(pady=20)

my_button.bind("<Enter>", change_pic)
my_button.bind("<Leave>", change_back)

root.mainloop()