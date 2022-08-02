'''
todo :  It is used to create a separate window container.
todo :  The toplevel widget is used when a python application needs to represent some extra information, pop-up, or the group of widgets on the new window.
'''

from tkinter import *

root = Tk()
root.geometry('400x400')

top = Toplevel()
top.title('New Window')

top.mainloop()