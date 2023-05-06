from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("750x450")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvariable=self.var, relief=FLAT, anchor='w')
        self.statusbar.pack(side=BOTTOM, fill=X)

    def click(self):
        Label(self, text="The button has been clicked").pack()

    def createButton(self, MyText):
        Button(self, text=MyText, command=self.click).pack()

if __name__ == '__main__':
    window = GUI()
    window.createButton("click")
    window.status()
    window.mainloop()
