from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("400x400")

def start_bar1():
    import time
    i = 1
    while i <= 110:
        progress1['value'] = i
        progress1.update_idletasks()
        i += 10
        time.sleep(0.2)

def start_bar2():
    import time
    i = 1
    while i <= 110:
        progress2['value'] = i
        progress2.update_idletasks()
        i += 10
        time.sleep(0.2)

progress1 = ttk.Progressbar(root, orient=HORIZONTAL, length=250, mode='indeterminate')
progress1.place(x=70, y=100)
Button(root, text='start', command=start_bar1).place(x=175, y=150)

progress2 = ttk.Progressbar(root, orient=HORIZONTAL, length=250, mode='determinate')
progress2.place(x=70, y=200)
Button(root, text='start', command=start_bar2).place(x=175, y=250)


root.mainloop()