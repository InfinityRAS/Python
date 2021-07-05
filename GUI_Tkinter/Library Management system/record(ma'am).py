from tkinter import *
from tkinter.messagebox import *


def Exit():
    a = askyesno("Exit", "Are you sure you want to Exit?")
    if a > 0:
        root.destroy()


def new():
    global file
    file = None
    nameEntry.delete(0, END)
    classEntry.delete(0, END)

    if teacherEntry.get() != 'Mr. Aryan Sisodiya':
        teacherEntry.delete(0, END)

    DateEntry.delete(0, END)
    Admn_Entry.delete(0, END)
    AllBookInfo_Entry.delete(1.0, END)
    Mobile_Entry.delete(0, END)


def reg():
    b = askyesno("Register Student", "Do you want to register the student?")
    if b > 0:
        with open("records.txt", "a") as f:
            f.write(f"\nDate:{DateEntry.get()}")
            f.write(f"\nThe name of the student is:{nameEntry.get()}")
            f.write(f"\nThe class and section of the student is:{classEntry.get()}")
            f.write(f"\nThe name of the teacher is:{teacherEntry.get()}")
            f.write(f"\nthe Admission Number of the student is:{Admn_Entry.get()}")
            f.write("\nInformation of book is: \n")
            inputValue = AllBookInfo_Entry.get("1.0", "end-1c")
            f.write(inputValue)
            f.write(f"\nMobile number of the student is:{Mobile_Entry.get()}")
            f.write("\n----------------------------------------------------------------------------------------------")

        kanha = Tk()
        kanha.geometry("1177x220")
        kanha.resizable(width=FALSE, height=FALSE)
        kanha.title("Library Management System- Students Record")
        # kanha.wm_iconbitmap("logo.ico")

        Label(kanha, text="Student has successfully Registered", bg="Dark Grey", fg="Blue",
              font=("Poor Richard", 62, "bold"),
              borderwidth=30, relief=SUNKEN).pack(fill=X)

        Button(kanha, text="Exit", bd=10, font=("Eras Bold ITC", 30), bg="Dark Green", relief=RAISED,
               fg="White", command=kanha.destroy).pack(anchor="ne")

        kanha.mainloop()


def Help():
    ashok = Tk()
    # ashok.wm_iconbitmap("logo.ico")
    ashok.geometry("650x312")
    ashok.title("Help")
    ashok.resizable(width=False, height=False)

    # ==============================================================================================================
    Label(ashok, text="Please visit our Official Website""\n 'www.aryan.sisodiya.com'", bg="Dark Grey",
          font=("Century Gothic", 25, "bold"), borderwidth=25, relief=SUNKEN).pack(fill=X)

    Label(ashok, text="for further help email us on""\n 'aryan.sisodiya@aryan.com'", bg="Dark Grey",
          font=("Century gothic", 25, "bold"), borderwidth=25, relief=RAISED).pack(fill=X)

    Button(ashok, text="Exit", bg="Dark Green", fg="White", font=("Eras Bold ITC", 22, "bold"), borderwidth=10,
           relief=RAISED, command=ashok.destroy).pack(anchor="ne")

    ashok.mainloop()


def feedback():
    def send():
        ask = askyesno("Send Feedback or Report Problem", "Do you want to send the feedback or problem reported?")
        if ask > 0:
            with open("records.txt", "a") as g:
                g.write("\n-------------------------------------------------------------------------------------------")
                g.write("\nFeedback send?: Yes")
                g.write(f"\nE-Mail Id of User is:{Aryan_Entry.get()}")
                g.write(f"\nReported problem or gave a feedback on date:{Date_Entry.get()}")
                inputValue = back_Entry.get("1.0", "end-1c")
                g.write("\nProblem reported or feedback given is:\n")
                g.write(inputValue)
                g.write("\n-------------------------------------------------------------------------------------------")

            # =========================================================================================================
            s = Tk()
            s.title("Send feedback or Report Problem")
            # s.wm_iconbitmap("logo.ico")
            s.geometry("856x200")
            s.resizable(width=False, height=False)

            Label(s, text="Thanks for your feedback", bg="Dark Grey", fg="Blue", font=("Poor Richard", 62, "bold"),
                  borderwidth=25, relief=SUNKEN).pack(fill=X)

            Button(s, text="Exit", bg="Dark Green", fg="White", font=("Eras Bold ITC", 22, "bold"), borderwidth=10,
                   relief=RAISED, command=s.destroy).pack(anchor="ne")

            feed.destroy()

            s.mainloop()

    # ===========================================================================================================
    def feed_Exit():
        b = askyesno("Exit", "Are you sure you want to exit?")
        if b > 0:
            feed.destroy()

    # ================================== Feedback ================================================================
    feed = Tk()
    feed.title("Send Feedback or Report Problem")
    # feed.wm_iconbitmap("logo.ico")
    feed.geometry("1315x640")
    feed.resizable(width=False, height=False)

    # ===========================================================================================================
    Label(feed, text="Send Feedback or Report Problem", bg="Dark Grey", fg="Blue", font=("Poor Richard", 62, "bold"),
          borderwidth=25,
          relief=RIDGE).pack(fill=X)

    f6 = Frame(feed, borderwidth=20, bg="Light Grey", relief=RAISED)
    f6.pack(anchor="nw", fill=X)

    f5 = Frame(f6)
    f5.grid(row=3, column=1)

    Aryan = Label(f6, text="Write your email ID:", bg="Powder Blue", fg="Red", font=("Century Gothic", 20, "bold"),
                  borderwidth=10, relief=SUNKEN, justify=LEFT)

    Date = Label(f6, text="Write today's date:", bg="Powder Blue", fg="Red", font=("Century Gothic", 20, "bold"),
                 borderwidth=10, relief=SUNKEN, justify=LEFT)

    back = Label(f6, text="Write your feedback""\n Or problem here:", bg="Powder Blue", fg="Red",
                 font=("Century gothic", 20, "bold"), borderwidth=10, relief=SUNKEN, justify=LEFT)

    Choose = Label(f6, text="What do you want to do?""\n Please Choose:", bg="Powder Blue", fg="Red",
                   font=("Century gothic", 20, "bold"), borderwidth=10, relief=SUNKEN, justify=LEFT)

    Date.grid(row=1, column=0)
    Aryan.grid(row=0, column=0)
    back.grid(row=3, column=0)
    Choose.grid(row=2, column=0)

    # =================================================================================================================
    Aryan_value = StringVar()
    Date_value = StringVar()

    scrollbar = Scrollbar(f5)
    scrollbar.pack(side=RIGHT, fill=Y)

    Aryan_Entry = Entry(f6, text=Aryan_value, font=("Arial", 20, "bold"), width=60, borderwidth=10, relief=RAISED,
                        fg="Black")
    Date_Entry = Entry(f6, text=Date_value, font=("Arial", 20, "bold"), width=60, borderwidth=10, relief=RAISED,
                       fg="Black")
    back_Entry = Text(f5, height=5, width=58, bd=10, relief=RAISED, fg="Black", font=("Arial", 20, "bold"),
                      yscrollcommand=scrollbar.set)

    scrollbar.config(command=back_Entry.yview)

    Aryan_Entry.grid(row=0, column=1)
    Date_Entry.grid(row=1, column=1)
    back_Entry.pack()

    # ========================================= DropDown Menu =======================================================
    options = ["Send a Feedback", "Report Problem"]
    clicked = StringVar(f6)

    clicked.set("Choose")
    drop = OptionMenu(f6, clicked, *options)
    drop.grid(row=2, column=1)
    drop.configure(font=("Century Gothic", 25, "bold"), width=40, bg="Dark Blue", fg="White", bd=10)

    # ================================================================================================================
    Button(feed, text="Send", fg="White", bg="Dark Green", font=("Century Gothic", 25, "bold"), borderwidth=10,
           command=send, height=10).pack(side=BOTTOM, anchor="se")

    Menubar_1 = Menu(feed)
    Menubar_1.add_cascade(label="Exit", command=feed_Exit)
    feed.config(menu=Menubar_1)

    feed.mainloop()


def about():
    a = Tk()
    a.geometry("1327x442")
    a.title("About")
    # a.wm_iconbitmap("logo.ico")
    a.resizable(width=False, height=False)

    # ===========================================================================================================
    Label(a, text="About Library Management System", bg="Dark Grey", fg="Blue", font=("Poor Richard", 62, "bold"),
          borderwidth=25, relief=RIDGE).pack(fill=X)

    Frame2 = Frame(a, borderwidth=20, bg="Dark Green", relief=RAISED)
    Frame2.pack(fill=X)

    Label(Frame2, text="Created by 'Aryan Sisodiya'""\n Version 5.0"
                       "\n All Copyrights reserved""\n If you want to see about license and further help."
                       " Kindly visit our official website""\n 'www.application.aryan.official.com'", bg="Dark Green",
          fg="White", font=("Century Gothic", 25, "bold")).pack()

    Button(a, text="Exit", bg="Dark Blue", fg="White", font=("Eras Bold ITC", 22, "bold"), borderwidth=10,
           relief=RAISED, command=a.destroy).pack(anchor="ne")

    a.mainloop()


# ====================================================== Main GUI ==========================================
if __name__ == "__main__":
    root = Tk()
    root.title("Library Management System- Students Record")
    # root.wm_iconbitmap("logo.ico")
    file = None

    # =================================================================MenuBar ====================================
    Menubar = Menu(root)
    m1 = Menu(Menubar, tearoff=0, bg="Light Grey", font=("Eras Bold ITC", 11))
    m1.add_command(label="Help", command=Help)
    m1.add_command(label="Send Feedback or Report Problem", command=feedback)
    m1.add_separator()
    m1.add_command(label="About", command=about)
    m1.add_command(label="Exit", command=Exit)
    Menubar.add_cascade(label="More", menu=m1)

    root.config(menu=Menubar)

    # ===============================================================================================================

    f2 = Frame(root, bg="Dark Grey", bd=20, relief=RIDGE)
    f2.pack(fill=X)

    Label(f2, text="Welcome to Application Aryan Official", font=("Poor Richard", 62, "bold"), fg="Blue",
          bg="Dark Grey").pack()

    f4 = Frame(root)
    f4.pack(side=RIGHT, fill=Y)

    aditya = Button(f4, text="Register", bd=15, font=("Eras Bold ITC", 30), bg="Dark Green", relief=RAISED, fg="White",
                    command=reg)
    aditya.pack(side=BOTTOM, anchor="se", fill=X)

    adithya = Button(f4, text="New", bd=15, font=("Eras Bold ITC", 30), bg="Dark Green", relief=RAISED, fg="White",
                     command=new)
    adithya.pack(side=BOTTOM, anchor="se", fill=X)

    f3 = Frame(root, borderwidth=20, bg="Light Grey", relief=RAISED)
    f3.pack(anchor="nw")

    # =============================================== labels ==========================================================
    name_label = Label(f3, text="Write student's name:", font=("Century Gothic", 20, "bold"),
                       borderwidth=10, relief=SUNKEN, justify=LEFT, bg="Powder Blue", fg="Red")

    class_label = Label(f3, text="Write student's class and section:", font=("Century Gothic", 20, "bold"),
                        bd=10, relief=SUNKEN, justify=LEFT, bg="Powder Blue", fg="Red")

    teacher_label = Label(f3, text="Write teacher's name:", font=("Century Gothic", 20, "bold"),
                          bd=10, relief=SUNKEN, justify=LEFT, bg="Powder Blue", fg="Red")

    date_label = Label(f3, text="Write the date:", font=("Century Gothic", 20, "bold"),
                       bd=10, relief=SUNKEN, justify=LEFT, bg="Powder Blue", fg="Red")

    Admn_label = Label(f3, text="Write student's admission number:", font=("Century Gothic", 20, "bold"),
                       bd=10, relief=SUNKEN, justify=LEFT, bg="Powder Blue", fg="Red")

    AllBookInfo_label = Label(f3, text="Write everything about the book \nwith number of books:",
                              font=("Century Gothic", 20, "bold"),
                              bd=10, relief=SUNKEN, justify=LEFT, bg="Powder Blue", fg="Red")

    Mobile_label = Label(f3, text="Write student's mobile number:", font=("Century Gothic", 20, "bold"),
                         bd=10, relief=SUNKEN, justify=LEFT, bg="Powder Blue", fg="Red")

    name_label.grid(row=0, column=0)
    class_label.grid(row=1, column=0)
    teacher_label.grid(row=2, column=0)
    date_label.grid(row=3, column=0)
    AllBookInfo_label.grid(row=6, column=0)
    Admn_label.grid(row=4, column=0)
    Mobile_label.grid(row=5, column=0)

    # ============================================= Scroll Bar ========================================================
    f4 = Frame(f3)
    f4.grid(row=6, column=1)

    scrollBar = Scrollbar(f4)
    scrollBar.pack(side=RIGHT, fill=Y)

    # ============================================= Entries ===========================================================
    nameVar = StringVar()
    ClassVar = StringVar()
    secVar = StringVar()
    DateVar = StringVar()

    nameEntry = Entry(f3, text="nameVar", font=("Arial", 20, "bold"), width=40, borderwidth=10, relief=RAISED,
                      fg="Black")
    classEntry = Entry(f3, text="ClassVar", font=("Arial", 20, "bold"), width=40, borderwidth=10, relief=RAISED,
                       fg="Black")

    teacherEntry = Entry(f3, text="SecVar", font=("Arial", 20, "bold"), width=40, borderwidth=10, relief=RAISED,
                         fg="Black")
    teacherEntry.insert(8, "Mr. Aryan Sisodiya")

    DateEntry = Entry(f3, text="DateVar", font=("Arial", 20, "bold"), width=40, borderwidth=10, relief=RAISED,
                      fg="Black")

    Admn_Entry = Entry(f3, text="AdmnVar", font=("Arial", 20, "bold"), width=40, borderwidth=10, relief=RAISED,
                       fg="Black")

    AllBookInfo_Entry = Text(f4, height=5, width=39, bd=10, relief=RAISED, fg="Black", font=("Arial", 20, "bold"),
                             yscrollcommand=scrollBar.set)

    Mobile_Entry = Entry(f3, text="MobileVar", font=("Arial", 20, "bold"), width=40, borderwidth=10, relief=RAISED,
                         fg="Black")

    scrollBar.config(command=AllBookInfo_Entry.yview)

    AllBookInfo_Entry.pack()
    nameEntry.grid(row=0, column=1)
    classEntry.grid(row=1, column=1)
    teacherEntry.grid(row=2, column=1)
    DateEntry.grid(row=3, column=1)
    Admn_Entry.grid(row=4, column=1)
    Mobile_Entry.grid(row=5, column=1)

    root.mainloop()
