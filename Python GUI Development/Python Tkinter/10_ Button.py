from tkinter import *
root = Tk()
root.geometry("543x150")
root.resizable(0,0)

frame = Frame(root, borderwidth=1.5, bg="light blue", relief=SUNKEN)
frame.pack(side=LEFT, anchor='nw')
My_Label = Label(root, text="THIS IS A SIMPE COLOR LIST").place(x=185, y=80)

def black_color():
    new_root = Tk()
    new_root.geometry('200x80')
    new_root.resizable(0,0)
    label = Label(new_root, text="This is Black color", font=("Aparajita", 18), fg="black")
    label.pack()

def magenta_color():
    new_root = Tk()
    new_root.geometry('200x80')
    new_root.resizable(0,0)
    label = Label(new_root, text="This is Magenta color", font=("Aparajita", 18), fg="magenta")
    label.pack()

def blue_color():
    new_root = Tk()
    new_root.geometry('200x80')
    new_root.resizable(0,0)
    label = Label(new_root, text="This is Blue color", font=("Aparajita", 18), fg="blue")
    label.pack()

def green_color():
    new_root = Tk()
    new_root.geometry('200x80')
    new_root.resizable(0,0)
    label = Label(new_root, text="This is Green color", font=("Aparajita", 18), fg="green")
    label.pack()

def yellow_color():
    new_root = Tk()
    new_root.geometry('200x80')
    new_root.resizable(0,0)
    label = Label(new_root, text="This is Yellow color", font=("Aparajita", 18), fg="yellow", bg='black')
    label.pack()

def Pink_color():
    new_root = Tk()
    new_root.geometry('200x80')
    new_root.resizable(0,0)
    label = Label(new_root, text="This is Pink color", font=("Aparajita", 18), fg="Pink")
    label.pack()

def Orange_color():
    new_root = Tk()
    new_root.geometry('200x80')
    new_root.resizable(0,0)
    label = Label(new_root, text="This is Orange color", font=("Aparajita", 18), fg="Orange")
    label.pack()

def Purple_color():
    new_root = Tk()
    new_root.geometry('200x80')
    new_root.resizable(0,0)
    label = Label(new_root, text="This is Purple color", font=("Aparajita", 18), fg="Purple")
    label.pack()

def red_color():
    new_root = Tk()
    new_root.geometry('200x80')
    new_root.resizable(0,0)
    label = Label(new_root, text="This is Red color", font=("Aparajita", 18), fg="Red")
    label.pack()

def White_color():
    new_root = Tk()
    new_root.geometry('200x80')
    new_root.resizable(0,0)
    label = Label(new_root, text="This is White color", font=("Aparajita", 18), fg="White", bg='black')
    label.pack()

b1 = Button(frame, fg="black", bg="white", activebackground="black", activeforeground="white", text="BLACK", command=black_color)
b1.pack(side=LEFT, padx=2.5)
b2 = Button(frame, fg="magenta", bg="white", activebackground="black", activeforeground="white", text="MAGENTA", command=magenta_color)
b2.pack(side=LEFT, padx=2.5)
b3 = Button(frame, fg="blue", bg="white", activebackground="black", activeforeground="white", text="BLUE", command=blue_color)
b3.pack(side=LEFT, padx=2.5)
b4 = Button(frame, fg="green", bg="white", activebackground="black", activeforeground="white", text="GREEN", command=green_color)
b4.pack(side=LEFT, padx=2.5)
b5 = Button(frame, fg="yellow", bg="black", activebackground="black", activeforeground="white", text="YELLOW", command=yellow_color)
b5.pack(side=LEFT, padx=2.5)
b6 = Button(frame, fg="white", bg="black", activebackground="black", activeforeground="white", text="WHITE", command=White_color)
b6.pack(side=LEFT, padx=2.5)
b7 = Button(frame, fg="orange", bg="white", activebackground="black", activeforeground="white", text="ORANGE", command=Orange_color)
b7.pack(side=LEFT, padx=2.5)
b8 = Button(frame, fg="purple", bg="white", activebackground="black", activeforeground="white", text="PURPLE", command=Purple_color)
b8.pack(side=LEFT, padx=2.5)
b9 = Button(frame, fg="red", bg="white", activebackground="black", activeforeground="white", text="RED", command=red_color)
b9.pack(side=LEFT, padx=2.5)
b10 = Button(frame, fg="pink", bg="white", activebackground="black", activeforeground="white", text="PINK", command=Pink_color)
b10.pack(side=LEFT, padx=2.5)

root.mainloop()
