'''The canvas widget is used to add the structured graphics to the python application. It is used to draw the graph and plots to the python application.'''
from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.resizable(0,0)

# Creating a canvas
canvas_widget = Canvas(root, width=canvas_width, height=canvas_height, bg="pink")
canvas_widget.pack()

# The line goes from the point x1, y1 to x2, y2.
canvas_widget.create_line(0, 0, 800, 400, fill="red")
canvas_widget.create_line(0, 400, 800, 0, fill="Red")

# To create a rectangle specify parameters in this order --> coordinates of top left and coordinates of bottom right
canvas_widget.create_rectangle(20, 20, 780, 380, fill="light blue")

# Creating an oval
canvas_widget.create_oval(20, 20, 780, 380, fill="sky blue")

# Creating an arc
canvas_widget.create_arc(50, 50, 750, 400, fill="light blue")

# Write a text on our window
canvas_widget.create_text(400, 200, text="The Python", font=("Poor Richard", 35))

root.mainloop()
