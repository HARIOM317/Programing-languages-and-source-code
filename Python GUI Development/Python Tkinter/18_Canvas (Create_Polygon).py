from tkinter import *
root = Tk()
canvas = Canvas(width=600, height=300, bg='yellow')
canvas.pack()

points1 = [250, 110, 480, 200, 280, 280, 250, 110]  # canvas 1
points2 = [10, 10, 250, 280, 50, 150, 20, 160, 10, 10]  # Canvas 2

canvas.create_polygon(points1, fill='orange', outline='red')
canvas.create_polygon(points2, fill='orange', outline='red')

root.mainloop()