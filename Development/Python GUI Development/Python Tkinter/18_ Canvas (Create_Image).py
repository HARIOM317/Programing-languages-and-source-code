from tkinter import *
root = Tk()
canvas = Canvas(width=400, height=300, bg='yellow')
canvas.pack()
photo = PhotoImage(file="A:\\Python Tutorial\\My Python Projects\\GUI\\03.gif")
canvas.create_image(5, 5, image=photo, anchor=NW)

root.mainloop()