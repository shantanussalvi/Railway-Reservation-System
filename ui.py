from email.mime import application
from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time

class Train:
    def __init__(self, root):
        self.root = root
        self.root.title = ("Railway Reservation System")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background="grey")

        Mainframe = Frame(self.root, bd=10, width=1350, height=700, bg="grey", relief=RIDGE)
        Mainframe.grid()

        Topframe1 = Frame(Mainframe, bd=10, width=1340, height=100, bg="grey", relief=RIDGE)
        Topframe1.grid()

        Topframe2 = Frame(Mainframe, bd=10, width=1300, height=500, bg="grey", relief=RIDGE)
        Topframe2.grid()

        f1 = Frame(Topframe2, width=890, height=500, bd=5, relief=RIDGE)
        f1.grid(row=1, column=0)

        f2 = Frame(Topframe2, width=400, height=500, pady=2, bd=5, relief=RIDGE)
        f2.grid(row=1, column=1)

        frametopRight = Frame (f2, width=404, height=420, bd=5, relief=RIDGE) 
        frametopRight.pack(side=TOP)

        frameBottomRight = Frame (f2, width=400, height=100, bd=5, pady=15, relief=RIDGE)
        frameBottomRight.pack (side=BOTTOM)

        f1a = Frame (f1, width=900, height=330, bd=5, relief=RIDGE) 
        f1a.pack (side=TOP) 
        f2a = Frame (f1, width=900, height=320, bd=5, relief=RIDGE) 
        f2a.pack (side=BOTTOM)

        toplefti = Frame (f1a, width=300, height=200, bd=5, padx=20, pady=1, relief=RIDGE) 
        toplefti.pack(side=LEFT)

        topleft2 = Frame (f1a, width=300,height=200, bd=5, relief=RIDGE)
        topleft2.pack(side=RIGHT)
        topleft3 = Frame (f1a, width=300, height=200, bd=5, pady=5, relief=RIDGE) 
        topleft3.pack (side=RIGHT)

        bottomlefti=Frame (f2a, width=450, height=300, bd=5,pady=12, relief=RIDGE) 

        bottomleft2 = Frame (f2a, width=450, height=300, bd=5, relief=RIDGE) 
        bottomleft2.pack(side=RIGHT)

        lblTitle = Label(Topframe1, font=('aerial', 40, 'bold'), text="Train Reservation System", bd=5, width=41, padx=4, )
    
if(__name__ == '__main__'):
    root = Tk()
    application = Train(root)
    root.mainloop()