from tkinter import *
import time

root = Tk()

root.geometry("359x150+0+0")
root.configure(background="Black")
root.resizable(0, 0)    # cannot resize or fix the size
# root.overrideredirect(1)      # hide the title bar

def start():
    text = time.strftime("%H:%M:%S")
    label.config(text=text)
    label.after(200, start)

label = Label(root, font=("Georgia", 50, "bold"), bg="black", fg="red", bd=50)
label.grid(row=0, column=1)
start()
root.mainloop()
