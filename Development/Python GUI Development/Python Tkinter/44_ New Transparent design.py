from tkinter import *
root = Tk()
root.configure(bg='sky blue')
root.geometry('800x500')
# root.attributes('-alpha', 0.5)
root.wm_attributes('-transparentcolor', root['bg'])   # Make transparent to root background color

my_frame = Frame(root, width=200, height=200, bg='sky blue')
my_frame.pack(pady=20, ipadx=15, ipady=15)

myLabel = Label(my_frame, text="Hello Friends...", font=("Poor Richard", 25, "bold"), bg="sky blue", fg="Red")
myLabel.pack(pady=20)

root.mainloop()
