from tkinter import *
root = Tk()
root.geometry('1000x600')

Width = 800
Height = 600
x = Width/2
y = Height/2

my_canvas = Canvas(root, width=Width, height=Height, bg='white')
my_canvas.pack()

# Add Image to Canvas
img = PhotoImage(file='A:\\Python GUI Development\\Python Tkinter\\Required Images\\1.png')
my_image = my_canvas.create_image(150, 130, anchor=NW, image=img)

# Move canvas using arrow key
def left(event):
    x = -10
    y = 0
    my_canvas.move(my_image, x, y)

def right(event):
    x = 10
    y = 0
    my_canvas.move(my_image, x, y)

def up(event):
    x = 0
    y = -10
    my_canvas.move(my_image, x, y)

def down(event):
    x = 0
    y = 10
    my_canvas.move(my_image, x, y)

# Move canvas using specific key
def pressing(event):
    x = 0
    y = 0
    if event.char == 'l': x = -10
    if event.char == 'r': x = 10
    if event.char == 'u': y = -10
    if event.char == 'd': y = 10
    my_canvas.move(my_image, x, y)

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("<Key>", pressing)



root.mainloop()