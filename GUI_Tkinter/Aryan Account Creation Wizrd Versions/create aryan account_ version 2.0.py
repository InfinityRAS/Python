from tkinter import *

root = Tk()

root.title("Account Creation")
root.geometry("1366x700")
root.minsize(1366, 700)
root.maxsize(1366, 700)
root.wm_iconbitmap("logo.ico")

title_label = Label(root, text="Welcome to Application Aryan Official", fg="Blue", bg="Dark Grey",
                    font=("Poor Richard", 62, "bold"), borderwidth=25, relief=RAISED, height=1, width=40)
title_label.pack(fill=X)

f1 = Frame(root, borderwidth=20, bg="Light Grey", relief=RAISED)
f1.pack(side=TOP)

Label1 = Label(root, text="Please NOTE:""\n Your Aryan ID should end with '@aryan.com'"
                          "\n Otherwise your Account will not be recognized as Aryan Account and will be deleted soon",
               width=62, height=3, bd=10, relief=SUNKEN, bg="Red", fg="White",
               font=("Century Gothic", 20, "bold"))
Label1.pack(fill=X)

user = Label(f1, text="Create your User Name:", bg="Powder Blue", fg="Red", font=("Century Gothic", 20, "bold"),
             borderwidth=10, relief=SUNKEN, justify=LEFT)
aryanID = Label(f1, text="Create your Aryan ID:", bg="Powder Blue", fg="Red", font=("Century Gothic", 20, "bold"),
                borderwidth=10, relief=SUNKEN, justify=LEFT)
password = Label(f1, text="Create a password:", bg="Powder Blue", fg="Red", font=("Century Gothic", 20, "bold"),
                 borderwidth=10, relief=SUNKEN)
DOB = Label(f1, text="Enter  your Date Of Birth""\n Please note down the correct format: 'DD MM YYYY'""\n"
                     " Otherwise your Account will be deactivated soon", bg="Powder Blue", fg="Red",
            font=("Century Gothic", 20, "bold"),
            borderwidth=10, relief=SUNKEN, justify=LEFT)

Terms_Confirm = Label(f1, text="Please confirm whether you follow our Terms and"
                               "\n Condition. Please answer in Yes or no", bg="Powder Blue", fg="Red",
                      font=("Century Gothic", 20, "bold"), borderwidth=10, relief=SUNKEN, justify=LEFT)
Terms_Confirm.grid(row=4, column=0)

user.grid(row=0, column=0, padx=0)
aryanID.grid(row=1, column=0)
password.grid(row=2, column=0)
DOB.grid(row=3, column=0)

uservalue = StringVar()
IDvalue = StringVar()
passvalue = StringVar()
DOB_value = StringVar()
Terms_Confirm_value = StringVar()

userEntry = Entry(f1, text="uservalue", font=("Arial", 20, "bold"), width=40, borderwidth=10, relief=RAISED, fg="Black")
IDEntry = Entry(f1, text="IDvalue", font=("Arial", 20, "bold"), width=40, borderwidth=10, relief=RAISED, fg="Black")
passEntry = Entry(f1, text="passvalue", font=("Arial", 20, "bold"), width=40, borderwidth=10, relief=RAISED, fg="Black")
DOBEntry = Entry(f1, text="DOB_Entry", font=("Arial", 20, "bold"), width=30, borderwidth=10, relief=RAISED, fg="Black")

DOBEntry.grid(column=2, row=3)
userEntry.grid(row=0, column=2)
IDEntry.grid(row=1, column=2)
passEntry.grid(row=2, column=2)

# =============================== Conclusion =========================================


def create():
    print(f"The UserName is {userEntry.get()}")
    print(f"The Aryan ID is {IDEntry.get()}")
    print(f"The Password is {passEntry.get()}")
    print(f"The Date of Birth of User is {DOBEntry.get()}")
    print(f"Are the User agrees our Terms and Conditions?: {Confirm.get()}")

    if Confirm.get() == 'Yes':
        print("Is the Account Created?: Yes")
        print("-------------------------------------------------------------------------------------")
        aryan = Tk()
        aryan.title("Aryan Account Creation")
        aryan.geometry("1366x700")
        aryan.minsize(1366, 700)
        aryan.maxsize(1366, 700)
        aryan.wm_iconbitmap("logo.ico")

        title = Label(aryan, text="Welcome to Application Aryan Official", fg="Blue", bg="Dark Grey",
                      font=("Poor Richard", 62, "bold"), borderwidth=25, relief=RAISED, height=1, width=40)
        title.pack(fill=X)

        Label(aryan, text="Successfully Created your Account!!!""\n Thanks for Choosing""\n Application Aryan Official",
              bg="Red", fg="White", borderwidth=10, font=("Century Gothic", 50, "bold"), relief=SUNKEN).pack(fill=X)

        Label(aryan, text="Now you can enjoy by""\n Signing in to Devices", bg="Blue", fg="White", borderwidth=30,
              font=("Copperplate Gothic Bold", 70, "bold"), relief=RAISED).pack(side=BOTTOM, anchor="sw", fill=X)

        aryan.mainloop()

    else:
        print("Is the account created?: No")
        print("-------------------------------------------------------------------------------------")
        aditya = Tk()
        aditya.title("Aryan Account Creation")
        aditya.geometry("1366x700")
        aditya.minsize(1366, 700)
        aditya.maxsize(1366, 700)
        aditya.wm_iconbitmap("logo.ico")

        title = Label(aditya, text="Welcome to Application Aryan Official", fg="Blue", bg="Dark Grey",
                      font=("Poor Richard", 62, "bold"), borderwidth=25, relief=RAISED, height=1, width=40)
        title.pack(fill=X)

        Label(aditya, text="Can't Created your Account!!!""\n Account Creation Failed""\n Thanks for Choosing"
                           "\n Application Aryan Official",
              bg="Red", fg="White", borderwidth=30, font=("Century Gothic", 40, "bold"), relief=RAISED).pack(fill=X)

        Label(aditya, text="Please try again""\n Later", bg="Blue", fg="White", borderwidth=30,
              font=("Copperplate Gothic Bold", 60, "bold"), relief=RAISED).pack(side=BOTTOM, anchor="sw", fill=X)

        aditya.mainloop()


# ==================================================================================================================
Confirm = Entry(f1, text="Terms_Confirm_value", font=("Arial", 20, "bold"), width=30, borderwidth=10, relief=RAISED,
                fg="Black")
Confirm.grid(column=2, row=4)

Btn_Create = Button(root, text="Create Account", fg="White", bg="Dark Green", font=("Times New Roman", 20, "bold"),
                    borderwidth=10, command=create)
Btn_Create.pack(side=BOTTOM, anchor="se")


root.mainloop()
