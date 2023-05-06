from tkinter import *
root = Tk()
root.geometry('800x600')

Width = 600
Height = 400
x = Width/2
y = Height/2

my_canvas = Canvas(root, width=Width, height=Height, bg='white')
my_canvas.pack()

my_circle = my_canvas.create_oval(x, y, x+50, y+50)
my_rectangle = my_canvas.create_rectangle(x, y, x+50, y+50)

# Move canvas using arrow key
def left(event):
    x = -10
    y = 0
    my_canvas.move(my_circle, x, y)
    my_canvas.move(my_rectangle, x, y)

def right(event):
    x = 10
    y = 0
    my_canvas.move(my_circle, x, y)
    my_canvas.move(my_rectangle, x, y)

def up(event):
    x = 0
    y = -10
    my_canvas.move(my_circle, x, y)
    my_canvas.move(my_rectangle, x, y)

def down(event):
    x = 0
    y = 10
    my_canvas.move(my_circle, x, y)
    my_canvas.move(my_rectangle, x, y)

# Move canvas using specific key
def pressing(event):
    x = 0
    y = 0
    if event.char == 'l': x = -10
    if event.char == 'r': x = 10
    if event.char == 'u': y = -10
    if event.char == 'd': y = 10
    my_canvas.move(my_circle, x, y)
    my_canvas.move(my_rectangle, x, y)

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("<Key>", pressing)


root.mainloop()