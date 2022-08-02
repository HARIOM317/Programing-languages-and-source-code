from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry('500x400')

v = ['C', 'C++', 'PYTHON', 'JAVA', 'C#', 'RUBY', 'KOTLIN', 'R', 'JAVA SCRIPT', 'HTML', 'CSS', '.NET', 'VISUAL BASIC']

combo_box = Combobox(root, values=v, height=5, width=20)
combo_box.set('select')
combo_box.pack()

root.mainloop()