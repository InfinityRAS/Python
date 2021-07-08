from tkinter import *
from PIL import ImageTk


class login():
    def __init__(self, root):
        self.root = root
        self.root.title("Login system")
        self.root.geometry("1199x600+100+50")
        self.root.wm_resizable(0,0)
        Label(self.root).place(x=0, y=0, relwidth=1, relheight=1)

        f1 = Frame(self.root, bg="white")
        f1.place(x=150, y=150, height=340, width=500)

        title = Label(f1, text="Login Here", font="Impact 35 bold", fg="#d77337", bg="White")
        title.place(x=90, y=30)

        Label(f1, text="Account Sign in Area", font=("Goudy old style", 15, "bold"), fg="#d25d17", bg="White").place(x=90, y=100)

        Label(f1, text="User Name:", font=("Goudy old style", 15, "bold"), fg="gray", bg="White").place(x=90, y=140)

        

root = Tk()
obj = login(root)
root.mainloop()
