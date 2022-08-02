from tkinter import *
root = Tk()
root.geometry('400x400')

def move_app(e):
    root.geometry(f"+{e.x_root}+{e.y_root}")

def quitter(e):
    root.destroy()

# Remove title bar
root.overrideredirect(True)

# Create our own/fake title bar
title_bar = Frame(root, bg="orange", relief=RAISED, bd=1)
title_bar.pack(expand=1, fill=X)

# Bind the title bar
title_bar.bind("<B1-Motion>", move_app)

# Create title text
title_label = Label(title_bar, text="  My Title Bar...", bg="orange", fg="white")
title_label.pack(side=LEFT, pady=4)

# Create close button on titlebar
close_label = Label(title_bar, text='X', bg="orange", fg='blue', bd=0.5, relief=SUNKEN, pady=5, padx=10, font="Georgia 15 bold")
close_label.pack(side=RIGHT, pady=4)
close_label.bind("<Button-1>", quitter)

# Create close button
mybutton = Button(root, text="CLOSE", font="Helvetica 32", command=root.quit)
mybutton.pack(pady=150)

root.mainloop()