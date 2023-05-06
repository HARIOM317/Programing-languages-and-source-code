from tkinter import *
import tkinter.ttk as ttk
root = Tk()
root.configure(bg="dark blue")
root.geometry("500x600")
# value 0 is for completely transparent and 1 is for completely non-transparent window
root.attributes('-alpha', 0.88)

# Create slider function
def slider(x):
    root.attributes('-alpha', my_slider.get())
    slide_label.configure(text=str(round(my_slider.get(), 2)))

# Create makeSolid function
def make_Solid(Event):
    new.attributes('-alpha', 1.0)

# Create NewWindow function
def NewWindow():
    global new
    new = Toplevel()
    new.attributes('-alpha', 0.75)
    new.bind("<Button-1>", make_Solid)

myLabel = Label(root, text="Hello friends",  font="Aparajita 25")
myLabel.pack(pady=20)

# Create a slider
my_slider = ttk.Scale(root, from_=0.1, to=1.0, value=0.8, orient=HORIZONTAL, command=slider)
my_slider.pack(pady=20)

slide_label = Label(root)
slide_label.pack(pady=12)

# Create a new window button
new_window = Button(root, text="New Window", command=NewWindow)
new_window.pack(pady=20)

root.mainloop()
