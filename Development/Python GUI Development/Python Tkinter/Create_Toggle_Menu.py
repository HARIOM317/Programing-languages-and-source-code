from tkinter import *

root = Tk()
root.geometry('1000x550')
root.config(bg='#262626')
root.title("Toggle Menu")
root.resizable(0,0)

l1 = Label(root, text="Hariom\nSingh\nRajput", fg='white', bg='#262626')
l1.config(font=('Comic Sans MS', 90))
l1.place(x=320, y=0)

def toggle_menu():
    f1 = Frame(root, width=300, height=700, bg='#202020')
    f1.place(x=0, y=0)

    def button(x, y, text, activbcolor, bcolor, cmd):
        def on_press(e):
            myButton1['background'] = activbcolor     #ffcc66
            myButton1['foreground'] = 'white'
        def on_leave(e):
            myButton1['background'] = bcolor
            myButton1['foreground'] = 'white'

        myButton1 = Button(f1, text=text, width=34, height=2, justify=LEFT, fg='white', bd=0, bg=bcolor, activeforeground='white', activebackground=activbcolor, command=cmd, font='Georgia 10 bold')

        myButton1.bind('<Enter>', on_press)
        myButton1.bind('<Leave>', on_leave)

        myButton1.place(x=x, y=y)

    button(0, 100, "Home", '#2d2d2d', '#202020', None)
    button(0, 140, "Window", '#2d2d2d', '#202020', None)
    button(0, 180, "Insert", '#2d2d2d', '#202020', None)
    button(0, 220, "Print", '#2d2d2d', '#202020', None)
    button(0, 260, "Option", '#2d2d2d', '#202020', None)
    button(0, 300, "Exit", '#2d2d2d', '#202020', None)


    def delete():
        f1.destroy()

    Button(f1, text='''
    ————
    ————
    ————''', command=delete, activebackground='#202020', bg='#202020', fg='white', bd=0, activeforeground='white').place(x=0, y=10)

Button(root, command=toggle_menu, text='''
————
————
————''', bd=0, fg='white', bg='#262626', activebackground='#262626').place(x=10, y=10)

root.mainloop()