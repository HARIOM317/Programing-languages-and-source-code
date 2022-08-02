from tkinter import *
root = Tk()
root.configure(bg='sky blue')
root.geometry('800x500')
# root.attributes('-alpha', 0.5)
root.wm_attributes('-transparentcolor', 'red') # Make transparent to red background

my_frame = Frame(root, width=400, height=400, bg='red')
my_frame.pack(pady=20)

root.mainloop()
