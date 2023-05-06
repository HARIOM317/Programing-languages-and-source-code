from tkinter import *
import time

class Ball:
    def __init__(self, canvas, x, y, diameter, xvelocity, yvelocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)
        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xvelocity = -self.xvelocity
        if (coordinates[3] >= (self.canvas.winfo_height()) or coordinates[1]<0):
            self.yvelocity = -self.yvelocity

        self.canvas.move(self.image, self.xvelocity, self.yvelocity)


root = Tk()
root.config(bg='sky blue')
WIDTH = 500
HEIGHT = 500

Label(root, text="Multiple Ball Animation", font="Georgia 16", fg='dark blue', bg='sky blue').pack()
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

volly_ball = Ball(canvas, 0, 0, 100, 1, 1, 'pink')
tennis_ball = Ball(canvas, 0, 0, 50, 4, 3, 'yellow')
basket_ball = Ball(canvas, 0, 0, 125, 8, 7, 'orange')

Button(root, text='Close', pady=15, padx=15, bg='light green', command=exit).pack()

while True:
    volly_ball.move()
    tennis_ball.move()
    basket_ball.move()
    root.update()
    time.sleep(0.01)


root.mainloop()