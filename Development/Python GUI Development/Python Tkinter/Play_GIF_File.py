from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time

root = Tk()
root.geometry('600x450')
root.config(bg='black')
root.resizable(0, 0)

def play_gif():
    try:
        global img
        img = Image.open("A:\\Python Tutorial\\My Python Projects\\GUI\\03.gif")

        label = Label(root)
        label.place(x=0, y=0)

        for img in ImageSequence.Iterator(img):
            img = img.resize((600, 450))
            img = ImageTk.PhotoImage(img)

            label.config(image=img)
            root.update()
            time.sleep(0.01)
        root.after(0, play_gif)
    except Exception as e:
        print(e)

def exit():
    root.destroy()

Button(root, text='Play', command=play_gif, pady=15, padx=20, bg='sky blue').place(x=100, y=20)
Button(root, text='Exit', command=exit, padx=20, pady=15, bg='sky blue').place(x=200, y=20)

root.mainloop()