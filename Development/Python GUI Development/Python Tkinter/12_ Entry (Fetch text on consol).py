from tkinter import *
root = Tk()
root.geometry('200x200')

# __________________ First Method ____________________
def fetch_text():
    print("By using first method :  ", my_entry.get())

my_entry = Entry(root)
my_entry.pack()

Button(root, text='Fetch words', command=fetch_text).pack()

# __________________ Second Method ____________________
def fetch():
    print("By using second method : ", s.get())
s = StringVar()
entry = Entry(root, textvariable=s)
entry.pack()
Button(root, text="Fetch", command=fetch).pack()

root.mainloop()