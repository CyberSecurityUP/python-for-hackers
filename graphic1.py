#Desenvolver interfaces graficas (GUI) Graphic User Interfaces
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text='Hello World')
        self.msg["font"] = ("Arial", "12", "italic", "bold")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.msg["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack()
root = Tk()
Application(root)
root.mainloop()

