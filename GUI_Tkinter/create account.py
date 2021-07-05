from tkinter import *


def submit():
    print(f"The UserName is {userEntry.get()}")
    print(f"The Aryan ID is {IDEntry.get()}")
    print(f"The Password is {passEntry.get()}")
    print("--------------------------------------------------------------------------------------------")


root = Tk()

root.title("Create Aryan Account")
root.geometry("1258x333")
root.wm_iconbitmap("logo.ico")
root.minsize(1258, 333)

user = Label(root, text="Create your User Name:", bg="Powder Blue", fg="Red", font=("Century Gothic", 20, "bold"),
             borderwidth=10, relief=SUNKEN, justify=LEFT)
aryanID = Label(root, text="Create your Aryan ID:", bg="Powder Blue", fg="Red", font=("Century Gothic", 20, "bold"),
                borderwidth=10, relief=SUNKEN, justify=LEFT)
password = Label(root, text="Create a password:", bg="Powder Blue", fg="Red", font=("Century Gothic", 20, "bold"),
                 borderwidth=10, relief=SUNKEN)

user.grid(row=0, column=0, padx=0)
aryanID.grid(row=1, column=0)
password.grid(row=2, column=0)

uservalue = StringVar()
IDvalue = StringVar()
passvalue = StringVar()

userEntry = Entry(root, text="uservalue", font=("Arial", 20, "bold"), width=50, borderwidth=10, relief=RAISED,
                  fg="Black")
IDEntry = Entry(root, text="IDvalue", font=("Arial", 20, "bold"), width=50, borderwidth=10, relief=RAISED, fg="Black")
passEntry = Entry(root, text="passvalue", font=("Arial", 20, "bold"), width=50, borderwidth=10, relief=RAISED,
                  fg="Black")

userEntry.grid(row=0, column=2)
IDEntry.grid(row=1, column=2)
passEntry.grid(row=2, column=2)

a = Button(root, text="Submit", height=2, width=10, fg="Black", borderwidth=5, bg="Powder Blue",
           font=("Times New Roman", 15, "bold"),
           relief=SUNKEN, command=submit)
a.grid(row=6, column=1, pady=50, padx=1)

root.mainloop()
