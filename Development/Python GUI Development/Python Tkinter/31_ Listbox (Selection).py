from tkinter import *
root = Tk()
root.geometry('500x400')

def selection():
    select_item = l.curselection()
    print("You select the following items:")
    for item in select_item:
        print(l.get(item))

l = Listbox(root, width=40, height=15, selectmode=MULTIPLE)
l.insert(1, 'c')
l.insert(2, 'c++')
l.insert(3, 'java')
l.insert(4, 'python')
l.insert(5, 'R')
l.insert(6, 'C#')
l.insert(7, 'html')
l.insert(8, 'css')
l.insert(9, 'js')
l.insert(10, 'Ruby')
l.insert(11, 'kotlin')
l.insert(12, '.net')
l.pack()

Button(root, text="show selection", command=selection).pack()

root.mainloop()