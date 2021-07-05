from tkinter import *


# ================================ functions ==============================================
def about():
    a = Tk()
    a.geometry("1325x386")
    a.minsize(1325, 386)
    a.maxsize(1325, 386)
    a.title("About")
    a.wm_iconbitmap("logo.ico")

    # ===========================================================================================================
    Label(a, text="About Aryan Account Creation Wizard", bg="Dark Grey", fg="Blue", font=("Poor Richard", 62, "bold"),
          borderwidth=25, relief=SUNKEN).pack(fill=X)

    Frame2 = Frame(a, borderwidth=20, bg="Dark Green", relief=RAISED)
    Frame2.pack(fill=X)

    Label(Frame2, text="Created by 'Application Aryan Official Ltd'""\n Version 3.0"
                       "\n All Copyrights reserved""\n If you want to see about license."
                       " Kindly visit our official website""\n 'www.application.aryan.official.com'", bg="Dark Green",
          fg="White", font=("Century Gothic", 25, "bold")).pack()

    a.mainloop()


def Help():
    ashok = Tk()
    ashok.wm_iconbitmap("logo.ico")
    ashok.geometry("651x284")
    ashok.minsize(651, 284)
    ashok.maxsize(651, 284)
    ashok.title("Help")
    # ==============================================================================================================
    Label(ashok, text="Please visit our Official Website""\n 'www.application.aryan.official.com'", bg="Dark Grey",
          font=("Century Gothic", 25, "bold"), borderwidth=25, relief=SUNKEN).pack(fill=X)

    Label(ashok, text="for further help email us on""\n 'official.aryan@application.com'", bg="Dark Grey",
          font=("Century gothic", 25, "bold"), borderwidth=25, relief=RAISED).pack(fill=X)

    ashok.mainloop()


def feedback():
    def send():
        print("Feedback send?: Yes")
        print(f"A user of E-mail Id:'{Aryan_Entry.get()}', gave a feedback or reported a problem:'{back_Entry.get()}',"
              f"on date:'{Date_Entry.get()}'")
        print("------------------------------------------------------------------------------------------------------")
        s = Tk()
        s.title("Send feedback or Report Problem")
        # s.wm_iconbitmap("logo.ico")
        s.geometry("856x150")
        s.minsize(856, 150)
        s.maxsize(856, 150)

        Label(s, text="Thanks for your feedback", bg="Dark Grey", fg="Blue", font=("Poor Richard", 62, "bold"),
              borderwidth=25, relief=SUNKEN).pack(fill=X)

        feed.destroy()

        s.mainloop()

    # ================================== Feedback ================================================================
    feed = Tk()
    feed.title("Send Feedback or Report Problem")
    feed.wm_iconbitmap("logo.ico")
    feed.geometry("1317x415")
    feed.minsize(1317, 415)
    feed.maxsize(1317, 415)

    # ===========================================================================================================
    Label(feed, text="Send Feedback or Report Problem", bg="Dark Grey", fg="Blue", font=("Poor Richard", 62, "bold"),
          borderwidth=25,
          relief=SUNKEN).pack(fill=X)

    f4 = Frame(feed, borderwidth=20, bg="Light Grey", relief=RAISED)
    f4.pack(anchor="nw", fill=X)

    Aryan = Label(f4, text="Write your email ID:", bg="Powder Blue", fg="Red", font=("Century Gothic", 20, "bold"),
                  borderwidth=10, relief=SUNKEN, justify=LEFT)

    Date = Label(f4, text="Write today's date:", bg="Powder Blue", fg="Red", font=("Century Gothic", 20, "bold"),
                 borderwidth=10, relief=SUNKEN, justify=LEFT)

    back = Label(f4, text="Write your feedback here", bg="Powder Blue", fg="Red", font=("Century gothic", 20, "bold"),
                 borderwidth=10, relief=SUNKEN, justify=LEFT)
    Date.grid(row=1, column=0)
    Aryan.grid(row=0, column=0)
    back.grid(row=2, column=0)

    # =================================================================================================================
    Aryan_value = StringVar()
    Date_value = StringVar()
    back_value = StringVar()

    Aryan_Entry = Entry(f4, text=Aryan_value, font=("Arial", 20, "bold"), width=60, borderwidth=10, relief=RAISED,
                        fg="Black")
    Date_Entry = Entry(f4, text=Date_value, font=("Arial", 20, "bold"), width=60, borderwidth=10, relief=RAISED,
                       fg="Black")
    back_Entry = Entry(f4, text=back_value, font=("Arial", 20, "bold"), width=60, borderwidth=10, relief=RAISED,
                       fg="Black")

    Aryan_Entry.grid(row=0, column=1)
    Date_Entry.grid(row=1, column=1)
    back_Entry.grid(row=2, column=1)

    # ================================================================================================================
    Button(feed, text="Send", fg="White", bg="Dark Green", font=("Century Gothic", 25, "bold"), borderwidth=10,
           command=send, height=10).pack(side=BOTTOM, anchor="se")

    feed.mainloop()


# =================================== Main GUI ===================================================================
root = Tk()
root.title("Aryan Account Creation")
root.geometry("1366x700")
root.minsize(1366, 700)
root.maxsize(1366, 700)
root.wm_iconbitmap("logo.ico")

# ============================ Menu bar =========================================================

Menubar = Menu(root)
m1 = Menu(Menubar, tearoff=0, bg="Light Grey", font=("Eras Bold ITC", 11))
m1.add_command(label="Help", command=Help)
m1.add_command(label="Send Feedback or Report Problem", command=feedback)
m1.add_separator()
m1.add_command(label="About", command=about)
m1.add_command(label="Exit", command=exit)
Menubar.add_cascade(label="More", menu=m1)

root.config(menu=Menubar)

# ===============================================================================================
title_label = Label(root, text="Welcome to Application Aryan Official", fg="Blue", bg="Dark Grey",
                    font=("Poor Richard", 62, "bold"), borderwidth=25, relief=RAISED, height=1, width=40)
title_label.pack(fill=X)

f1 = Frame(root, borderwidth=20, bg="Light Grey", relief=RAISED)
f1.pack(side=TOP)

Label1 = Label(root, text="Please NOTE:""\n Your Aryan ID should end with '@aryan.com'"
                          "\n Otherwise your Account will not be recognized as Aryan Account and will be deleted soon",
               width=74, height=3, borderwidth=20, relief=SUNKEN, bg="Red", fg="White",
               font=("Century Gothic", 20, "bold"))
Label1.pack(side=LEFT, fill=Y)

# ================================================================================================================
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

# =================================================================================================================
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


# =============================== Conclusion ==========================================================
def create():
    """This will create a new Windows """
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

        # ==========================================================================================================
        title = Label(aryan, text="Welcome to Application Aryan Official", fg="Blue", bg="Dark Grey",
                      font=("Poor Richard", 62, "bold"), borderwidth=25, relief=RAISED, height=1, width=40)
        title.pack(fill=X)

        Label(aryan, text="Successfully Created your Account!!!""\n Thanks for Choosing""\n Application Aryan Official",
              bg="Red", fg="White", borderwidth=30, font=("Century Gothic", 50, "bold"), relief=RAISED).pack(fill=BOTH)

        Label(aryan, text="Now you can enjoy by""\n Signing in to Devices", bg="Blue", fg="White", borderwidth=30,
              font=("Copperplate Gothic Bold", 70, "bold"), relief=RAISED).pack(side=BOTTOM, anchor="sw", fill=X)

        # ================================== Menubar ==================================================
        Menubar_2 = Menu(aryan)
        m2 = Menu(Menubar_2, tearoff=0, bg="Light Grey", font=("Eras Bold ITC", 11))
        m2.add_command(label="Help", command=Help)
        m2.add_command(label="Send Feedback or Report Problem", command=feedback)
        m2.add_separator()
        m2.add_command(label="About", command=about)
        m2.add_command(label="Exit", command=aryan.destroy)
        Menubar_2.add_cascade(label="More", menu=m2)

        aryan.config(menu=Menubar_2)

        root.destroy()

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

        # ==================================================================================================
        title = Label(aditya, text="Welcome to Application Aryan Official", fg="Blue", bg="Dark Grey",
                      font=("Poor Richard", 62, "bold"), borderwidth=25, relief=RAISED, height=1, width=40)
        title.pack(fill=X)

        Label(aditya, text="Can't Created your Account!!!""\n Account Creation Failed""\n Thanks for Choosing"
                           "\n Application Aryan Official",
              bg="Red", fg="White", borderwidth=30, font=("Century Gothic", 40, "bold"), relief=RAISED).pack(fill=X)

        Label(aditya, text="Please try again""\n Later", bg="Blue", fg="White", borderwidth=30,
              font=("Copperplate Gothic Bold", 60, "bold"), relief=RAISED).pack(side=BOTTOM, anchor="sw", fill=X)

        # =================================== Menubar =========================================================
        Menubar_3 = Menu(aditya)
        m3 = Menu(Menubar_3, tearoff=0, bg="Light Grey", font=("Eras Bold ITC", 11))
        m3.add_command(label="Help", command=Help)
        m3.add_command(label="Send Feedback or Report Problem", command=feedback)
        m3.add_separator()
        m3.add_command(label="About", command=about)
        m3.add_command(label="Exit", command=aditya.destroy)
        Menubar_3.add_cascade(label="More", menu=m3)

        aditya.config(menu=Menubar_3)

        aditya.mainloop()


# ==================================================================================================================
Confirm = Entry(f1, text="Terms_Confirm_value", font=("Arial", 20, "bold"), width=30, borderwidth=10, relief=RAISED,
                fg="Black")
Confirm.grid(column=2, row=4)

Btn_Create = Button(root, text="Create""\n Accoun""\n-t", fg="White", bg="Dark Green",
                    font=("Eras Bold ITC", 20, "bold"),
                    borderwidth=10, command=create, height=10)
Btn_Create.pack(side=BOTTOM, anchor="se", fill=BOTH)

root.mainloop()
