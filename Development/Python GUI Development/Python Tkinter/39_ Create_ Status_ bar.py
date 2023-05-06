from tkinter import *

def upload():
    statusvar.set("Busy...")
    s_bar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready")

root = Tk()
root.geometry("400x400")

statusvar = StringVar()
statusvar.set("Ready")

s_bar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor='w')
s_bar.pack(side=BOTTOM, fill=X)

Button(root, text="Upload", command=upload).pack()

root.mainloop()
