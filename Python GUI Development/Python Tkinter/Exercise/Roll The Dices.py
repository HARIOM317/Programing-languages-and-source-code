from tkinter import *
import random

root = Tk()
root.geometry('1000x600')
root.title("Roll The Dice")

label = Label(root, text="", font="Georgia 160", fg='dark green')

def roll():
    # These all codes indicate 1, 2, 3, 4, 5, and 6 dots for dice.
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.config(text=f"{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}\n{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}")
    label.pack()


button = Button(root, text="Roll", width=10, height=2, font="georgia 12", bg='white', fg='orange', bd=0.5, command=roll)
button.pack(pady=10, padx=10)


root.mainloop()