from tkinter import *
from tkinter.messagebox import *


# =========================================== Functions ==============================================================
def number1():
    print(1)


def feedback():
    def retrieve_input():
        inputValue = back_Entry.get("1.0", "end-1c")
        print("Problem reported or feedback given is:")
        print(inputValue)

    def send():
        ask = askyesno("Send Feedback or Report Problem", "Do you want to send the feedback or problem reported?")
        if ask > 0:
            print("Feedback send?: Yes")
            print(f"E-Mail Id of User is:{Aryan_Entry.get()}")
            print(f"Reported problem or gave a feedback on date:{Date_Entry.get()}")
            retrieve_input()
            print("--------------------------------------------------------------------------------------------------")

            # =========================================================================================================
            s = Tk()
            s.title("Send feedback or Report Problem")
            s.wm_iconbitmap("logo.ico")
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
    feed.wm_iconbitmap("Calculator 2 logo.ico")
    feed.geometry("1315x640")
    feed.resizable(width=False, height=False)

    # ===========================================================================================================
    Label(feed, text="Send Feedback or Report Problem", bg="Dark Grey", fg="Blue", font=("Poor Richard", 62, "bold"),
          borderwidth=25,
          relief=RIDGE).pack(fill=X)

    f4 = Frame(feed, borderwidth=20, bg="Light Grey", relief=RAISED)
    f4.pack(anchor="nw", fill=X)

    f5 = Frame(f4)
    f5.grid(row=3, column=1)

    Aryan = Label(f4, text="Write your email ID:", bg="Powder Blue", fg="Red", font=("Century Gothic", 20, "bold"),
                  borderwidth=10, relief=SUNKEN, justify=LEFT)

    Date = Label(f4, text="Write today's date:", bg="Powder Blue", fg="Red", font=("Century Gothic", 20, "bold"),
                 borderwidth=10, relief=SUNKEN, justify=LEFT)

    back = Label(f4, text="Write your feedback""\n Or problem here:", bg="Powder Blue", fg="Red",
                 font=("Century gothic", 20, "bold"), borderwidth=10, relief=SUNKEN, justify=LEFT)

    Choose = Label(f4, text="What do you want to do?""\n Please Choose:", bg="Powder Blue", fg="Red",
                   font=("Century gothic", 20, "bold"), borderwidth=10, relief=SUNKEN, justify=LEFT)

    Date.grid(row=1, column=0)
    Aryan.grid(row=0, column=0)
    back.grid(row=3, column=0)
    Choose.grid(row=2, column=0)

    # =================================================================================================================
    Aryan_value = StringVar()
    Date_value = StringVar()

    scrollBar = Scrollbar(f5)
    scrollBar.pack(side=RIGHT, fill=Y)

    Aryan_Entry = Entry(f4, text=Aryan_value, font=("Arial", 20, "bold"), width=60, borderwidth=10, relief=RAISED,
                        fg="Black")
    Date_Entry = Entry(f4, text=Date_value, font=("Arial", 20, "bold"), width=60, borderwidth=10, relief=RAISED,
                       fg="Black")
    back_Entry = Text(f5, height=5, width=58, bd=10, relief=RAISED, fg="Black", font=("Arial", 20, "bold"),
                      yscrollcommand=scrollBar.set)

    scrollBar.config(command=back_Entry.yview)

    Aryan_Entry.grid(row=0, column=1)
    Date_Entry.grid(row=1, column=1)
    back_Entry.pack()

    # ========================================= DropDown Menu =======================================================
    options = ["Send a Feedback", "Report Problem"]
    clicked = StringVar(f4)

    clicked.set("Choose")
    drop = OptionMenu(f4, clicked, *options)
    drop.grid(row=2, column=1)
    drop.configure(font=("Century Gothic", 25, "bold"), width=40, bg="Dark Blue", fg="White", bd=10)

    # ================================================================================================================
    Button(feed, text="Send", fg="White", bg="Dark Green", font=("Century Gothic", 25, "bold"), borderwidth=10,
           command=send, height=10).pack(side=BOTTOM, anchor="se")

    Menubar_1 = Menu(feed)
    Menubar_1.add_cascade(label="Exit", command=feed_Exit)
    feed.config(menu=Menubar_1)

    feed.mainloop()


def number2():
    print(2)


def number3():
    print(3)


def number4():
    print(4)


def number5():
    print(5)


def number6():
    print(6)


def number7():
    print(7)


def number8():
    print(8)


def number9():
    print(9)


def number0():
    print(0)


def sqrt():
    print("√")


def add():
    print("+")


def sub():
    print("-")


def mul():
    print("*")


def div():
    print(chr(247))


def equals():
    print("=")


def dot():
    print(".")


def about():
    a = Tk()
    a.geometry("1091x445")
    a.title("About")
    a.wm_iconbitmap("Calculator 2 logo.ico")
    a.resizable(width=False, height=False)

    # ===========================================================================================================
    Label(a, text="About Calculator", bg="Dark Grey", fg="Blue", font=("Poor Richard", 62, "bold"),
          borderwidth=25, relief=SUNKEN).pack(fill=X)

    Frame2 = Frame(a, borderwidth=20, bg="Dark Green", relief=RAISED)
    Frame2.pack(fill=X)

    Label(Frame2, text="Created by 'Application Aryan Official Ltd'""\n Version 7.9"
                       "\n All Copyrights reserved""\n If you want to see about license."
                       " Kindly visit our official website""\n 'www.application.aryan.official.com'", bg="Dark Green",
          fg="White", font=("Century Gothic", 25, "bold")).pack()

    Button(a, text="Exit", bg="Dark Blue", fg="White", font=("Eras Bold ITC", 22, "bold"), borderwidth=10,
           relief=RAISED, command=a.destroy).pack(anchor="ne")

    a.mainloop()


def Help():
    ashok = Tk()
    ashok.wm_iconbitmap("Calculator 2 logo.ico")
    ashok.geometry("650x312")
    ashok.title("Help")
    ashok.resizable(width=False, height=False)

    # ==============================================================================================================
    Label(ashok, text="Please visit our Official Website""\n 'www.application.aryan.official.com'", bg="Dark Grey",
          font=("Century Gothic", 25, "bold"), borderwidth=25, relief=SUNKEN).pack(fill=X)

    Label(ashok, text="for further help email us on""\n 'official.aryan@application.com'", bg="Dark Grey",
          font=("Century gothic", 25, "bold"), borderwidth=25, relief=RAISED).pack(fill=X)

    Button(ashok, text="Exit", bg="Dark Green", fg="White", font=("Eras Bold ITC", 22, "bold"), borderwidth=10,
           relief=RAISED, command=ashok.destroy).pack(anchor="ne")

    ashok.mainloop()


def root_Exit():
    b = askyesno("Exit", "Are you sure you want to exit?")
    if b > 0:
        root.destroy()


# ===================================== Main GUI ==================================================
root = Tk()

root.title("Calculator")
root.geometry("914x625")
# root.resizable(width=False, height=False)
root.wm_iconbitmap("Calculator 2 logo.ico")

frame1 = Frame(root, bg="Light Green", borderwidth=50, relief=SUNKEN)
frame1.pack(anchor="n", fill=X)

greet = Entry(frame1, font=("Century Gothic", 50, "bold"),
              bg="Light green", fg="Black", justify=RIGHT)
greet.pack(fill=X)
greet.insert(0, "0")

frame2 = Frame(root, bg="Dark Grey", pady=1, padx=2)
frame2.pack()

# ====================================== BUTTONS ==========================================================
btn1 = Button(frame2, text="9", font=("Century Gothic", 50, "bold"), relief=RAISED, bg="Powder Blue",
              command=number9)
btn1.grid(row=0, column=2)

Button(frame2, text="8", font=("Century Gothic", 50, "bold"), bg="Powder Blue", relief=RAISED,
       command=number8).grid(row=0, column=1, pady=1, padx=1)

Button(frame2, text="7", font=("Century Gothic", 50, "bold"), bg="Powder Blue", relief=RAISED,
       command=number7).grid(row=0, column=0, pady=1, padx=1)

Button(frame2, text="6", font=("Century Gothic", 50, "bold"), bg="Powder Blue", relief=RAISED,
       command=number6).grid(row=1, column=2, pady=1, padx=1)

Button(frame2, text="5", font=("Century Gothic", 50, "bold"), bg="Powder Blue", relief=RAISED,
       command=number5).grid(row=1, column=1, pady=1, padx=1)

Button(frame2, text="4", font=("Century Gothic", 50, "bold"), bg="Powder Blue", relief=RAISED,
       command=number4).grid(row=1, column=0, pady=1, padx=1)

Button(frame2, text="3", font=("Century Gothic", 50, "bold"), bg="Powder Blue", relief=RAISED,
       command=number3).grid(row=2, column=2, pady=1, padx=1)

Button(frame2, text="2", font=("Century Gothic", 50, "bold"), bg="Powder Blue", relief=RAISED,
       command=number2).grid(row=2, column=1, pady=1, padx=1)

Button(frame2, text="1", font=("Century Gothic", 50, "bold"), bg="Powder Blue", relief=RAISED,
       command=number1).grid(row=2, column=0, pady=1, padx=1)

Button(frame2, text="+", font=("Century Gothic", 50, "bold"), bg="Dark Grey", relief=RAISED, width=5,
       command=add).grid(row=0, column=4, pady=1, padx=1)

Button(frame2, text="-", font=("Century Gothic", 52, "bold"), bg="Dark Grey", relief=RAISED,
       command=sub).grid(row=0, column=3, pady=2, padx=1)

Button(frame2, text="x", font=("Century Gothic", 50, "bold"), bg="Dark Grey", relief=RAISED,
       command=mul).grid(row=2, column=3, pady=1, padx=1)

Button(frame2, text="√", font=("Century Gothic", 50, "bold"), bg="Dark Grey", relief=RAISED, width=3,
       command=sqrt).grid(row=0, column=5, pady=1, padx=1)

Button(frame2, text="=", font=("Century Gothic", 50, "bold"), bg="Dark Grey", relief=RAISED, width=5,
       command=equals).grid(row=1, column=4, pady=1, padx=1)

Button(frame2, text=".", font=("Century Gothic", 52, "bold"), bg="Dark Grey", relief=RAISED, width=3,
       command=dot).grid(row=2, column=5, pady=1, padx=1)

Button(frame2, text=chr(247), font=("Century Gothic", 50, "bold"), bg="Dark Grey", relief=RAISED,
       width=5, command=div).grid(row=2, column=4, pady=1, padx=1)

Button(frame2, text="0", font=("Century Gothic", 50, "bold"), bg="Powder Blue", relief=RAISED,
       command=number0).grid(row=1, column=3, pady=1, padx=1)

# =================================================================================================================
Button(frame2, text="Feed""\n -Back", font=("Century Gothic", 26, "bold"), bg="Dark Red",
       relief=RAISED, command=feedback, fg="White").grid(row=1, column=5, pady=1, padx=1)

Button(frame2, text="Exit", font=("Century Gothic", 42, "bold"), bg="Dark Red", relief=RAISED,
       command=root_Exit, width=4, height=1, fg="White").grid(row=1, column=6, pady=1, padx=1)

Button(frame2, text="About", font=("Century Gothic", 25, "bold"), bg="Dark Red", relief=RAISED,
       command=about, height=3, width=6, fg="White").grid(row=2, column=6, pady=1, padx=1)

Button(frame2, text="Help", font=("Century Gothic", 30, "bold"), bg="Dark Red", relief=RAISED,
       command=Help, width=6, height=2, fg="White").grid(row=0, column=6)

root.mainloop()
