'''
TODO: --> The Menu widget is used to create various types of menus (top level, pull down, and pop up) in the python application.

The top-level menus are the one which is displayed just under the title bar of the parent window. We need to create a new instance of the Menu widget and add various commands to it by using the add() method.
'''

from tkinter import *

root = Tk()
root.geometry("824x412")
def myfunc():
    print("Hello, This is a function!")
def help():
    print("Tell me what can i do for you?")

# Create a non dropdown menu
mymenus = Menu(root)
mymenus.add_command(label='Hello', command=myfunc)
mymenus.add_command(label='Exit', command=quit)
mymenus.add_command(label='Help', command=help)
root.config(menu=mymenus)

root.mainloop()
