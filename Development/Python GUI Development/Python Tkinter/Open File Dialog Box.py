from tkinter import *
from tkinter import filedialog

def Ask_Open_File():
    result = filedialog.askopenfile(initialdir="/", title='Open File', filetypes=(("Text File", "*.txt"),
                                                                         ("All Files", "*.*")))
    data.insert(INSERT, result)

root = Tk()
root.geometry('200x200')
Button(root, text='Open File', command=Ask_Open_File).pack()
data = Text(root, width=50, height=25, wrap=WORD)
data.pack()

root.mainloop()
