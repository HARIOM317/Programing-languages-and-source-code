'''
todo --> The Scale widget is used to implement the graphical slider to the python application so that the user can slide through the range of values shown on the slider and select the one among them.
'''

from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Slider")

window_width = StringVar()
window_height = StringVar()

mySlider1 = Scale(root, from_=0, to=100, width=30, tickinterval=50).pack(side=LEFT)
mySlider2 = Scale(root, from_=0, to=500, orient=HORIZONTAL, width=30, tickinterval=250).pack(side=TOP)

root.mainloop()
