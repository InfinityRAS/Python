from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as tkmsbx

loginId = 'aryan.sisodiya1306987@aryan.com'
password = 'aryan.sis.1306987'

# ================================================= functions ========================================
global aryan_entry
global pass2_entry
def sign():
    if Aryan_Entry.get() == '' or pass_Entry.get() == '':
        tkmsbx.showerror("Sign In", "Both fields are reqiured")

    else:
        if Aryan_Entry.get() == loginId:
            if pass_Entry.get() == password:
                kanha = Tk()
                kanha.title("Aryan Account Sign In")
                kanha.iconbitmap("logo.ico")
                # kanha.geometry("")
                # kanha.resizable(0, 0)
                # ================================================= Menu Bar =================================
                Menubar_2 = Menu(kanha)
                m2 = Menu(Menubar_2, tearoff=0, bg="Light Grey", font=("Eras Bold ITC", 11))
                m2.add_command(label="Help", command=Help)
                m2.add_command(label="Send Feedback or Report Problem", command=feedback)
                m2.add_separator()
                m2.add_command(label="About", command=about)
                m2.add_command(label="Exit", command=kanha.destroy)
                Menubar_2.add_cascade(label="More", menu=m2)

                kanha.config(menu=Menubar_2)
                # =========================================== Labels =========================================
                Label(kanha, text="Welcome to Application Aryan Official",
                         fg="Blue", bg="Dark Grey",font=("Poor Richard", 62, "bold"), borderwidth=25, relief=RIDGE).pack(fill=X)

                Label(kanha, text="Hello, Mr. Aryan Sisodiya \nYou've successfully Signed In", bg="Red", fg="White", borderwidth=30,
                      font=("Century Gothic", 60, "bold"), relief=RAISED).pack(fill=X)

                Label(kanha, text="Thanks for Choosing \nApplication Aryan Official", bg="Blue", fg="White", borderwidth=30,
                      font=("Copperplate Gothic bold", 60, "bold"), relief=RAISED).pack(fill=X)

                Button(kanha, text="Exit", bd=10, font=("Eras Bold ITC", 25, "bold"), bg="Dark Green", relief=RAISED,
                        fg="White", command=kanha.destroy).pack(anchor="ne")


                root.destroy()
                kanha.mainloop()

            else:
                tkmsbx.showerror("Sign In", "Password is not correct")

        else:
            tkmsbx.showerror("Sign In", "Aryan Id is invalid")
    

def for_pass():
    def can():
        b = tkmsbx.askyesno("Forgot Password", "Are you sure you want to exit?")
        if b > 0:
            aryan.destroy()

    def Next():
        def reset():
            c = tkmsbx.askyesno("Reset Password", "Are you sure you want to reset your password?")
            if c > 0:
                if pass2_entry.get() == pass3_entry.get():
                    raj.destroy()
                    with open("Feedback_sign_in.txt", "a") as x:
                        x.write("\n-----------------------------------------------------------------")
                        x.write("\nPassword for Aryan Id:")
                        # get_pass1 = aryan_entry1.get()
                        x.write(aryan_entry1.get())
                        x.write("\nNow changed into:")
                        get_id = pass2_entry.get()
                        x.write(get_id)
                        x.write("\n------------------------------------------------------------------")
                        x.close()
                        
                    tkmsbx.showinfo("Reset Password", "Your Password has been successfully Changed!! \nThanks for choosing " 
                                "Application Aryan Official")

                elif pass2_entry.get() == '' or pass3_entry.get() == '':
                    tkmsbx.showerror("Reset Password", "Both fields are required")

                else:
                    tkmsbx.showerror("Reset Password", "Both Passwords are not same")

        if code_entry.get() == '':
            aryan.destroy()
            raj = Tk()
            raj.title("Reset Password")
            raj.wm_iconbitmap("logo.ico")
            raj.resizable(0, 0)

            Label(raj, text="Welcome to Application Aryan Official", font=("Poor Richard", 55, "bold"), bd=20, relief=RIDGE, 
                    fg="blue", bg="dark grey").pack(fill=X)
            
            f2 = Frame(raj, bd=20, bg="Dark grey", relief=RAISED)
            f2.pack(fill=X)

            Label(f2, text="Write your New password here:", font=("Century Gothic", 20, "bold"),
                    bd=15, fg="Red", bg="Powder Blue", relief=SUNKEN).grid(row=0, column=0)

            Label(f2, text="Write your New password again here:", font=("Century Gothic", 20, "bold"),
                    bd=15, fg="Red", bg="Powder Blue", relief=SUNKEN).grid(row=1, column=0)

            pass2Var = StringVar()
            pass3Var = StringVar()

            pass2_entry = Entry(f2, text="pass2Var",  font="Arial 20 bold", bd=10, fg="black", relief=RAISED, width=40)
            pass2_entry.grid(row=0, column=1)

            pass3_entry = Entry(f2, text="pass3Var",  font="Arial 20 bold", bd=10, fg="black", relief=RAISED, width=40)
            pass3_entry.grid(row=1, column=1)

            Button(raj, text="Reset Password", font=("Eras bold ITC", 25, "bold"), bd=15, 
                    bg="Dark Green", fg="White", command=reset).pack(side=BOTTOM, anchor="se")

            raj.mainloop()

            

        else:
            tkmsbx.showerror("Forgot password", "Invalid Security code")

    # ============================================ Forget Password ========================================
    a = tkmsbx.askokcancel("Forgot Password", "Are you sure you want \nto go with forgot password")
    if a > 0:
        def set_this():
            tkmsbx.showinfo("Forgot Password", f"This Aryan Id {aryan_entry1.get()} has been selected")

        aryan = Tk()
        aryan.title("Forgot Password")
        aryan.wm_iconbitmap("logo.ico")
        aryan.resizable(0, 0)
        
        a = Label(aryan, text="Welcome to Application Aryan Official", font=("Poor Richard", 55, "bold"), bd=20, relief=RIDGE, 
                fg="blue", bg="dark grey")
        a.pack(fill=X)

        f1 = Frame(aryan)
        f1.pack(side=LEFT)

        Label(f1, text="A security code has send to your Aryan Id \nKindly Enter it here:", font=("Century Gothic", 20, "bold"),
                bd=15, fg="Red", bg="Powder Blue", relief=SUNKEN).grid(row=1, column=0)

        Label(f1, text="Write your Aryan ID", font=("Century Gothic", 20, "bold"),
                bd=15, fg="Red", bg="Powder Blue", relief=SUNKEN).grid(row=0, column=0)

        codeVar = StringVar()
        AryanVar = StringVar()
        code_entry = Entry(f1, textvariable="codeVar", font="Arial 20 bold",
                            bd=10, fg="black", relief=RAISED)

        aryan_entry1 = Entry(f1, textvariable="AryanVar", font="Arial 20 bold",
                            bd=10, fg="black", relief=RAISED)
        aryan_entry1.grid(row=0, column=1)

        code_entry.grid(row=1, column=1)

        Button(aryan, text="Cancel", font=("Eras bold ITC", 20, "bold"), bd=15, width=7,
            bg="Dark Green", fg="White", command=can).pack()

        Button(aryan, text="Next", font=("Eras bold ITC", 20, "bold"), bd=15, width=7,
            bg="Dark Green", fg="White", command=Next).pack()

        Button(aryan, text="Set this \nAryan Id", font=("Eras bold ITC", 20, "bold"), bd=15, width=7,
            bg="Dark Green", fg="White", command=set_this).pack()

        aryan.mainloop()


def Help():
    ashok = Tk()
    ashok.wm_iconbitmap("logo.ico")
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


def feedback():
    def send():
        ask = tkmsbx.askyesno("Send Feedback or Report Problem", "Do you want to send the feedback or problem reported?")
        if ask > 0:
            with open("Feedback_sign_in.txt", "a") as d:
                d.write("\n---------------------------------------------------------------------------------------------")
                d.write("\nFeedback send?: Yes")
                d.write(f"\nE-Mail Id of User is:{Aryan_Entry.get()}")
                d.write(f"\nReported problem or gave a feedback on date:{Date_Entry.get()}")
                d.write("\n------------------------------------------------------------------------------------------")
                d.write("\nProblem reported or feedback given is:\n")
                d.write(back_Entry.get("1.0", "end-1c"))
                d.write("\n------------------------------------------------------------------------------------------")

                d.close()

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
        b = tkmsbx.askyesno("Exit", "Are you sure you want to exit?")
        if b > 0:
            feed.destroy()

    # ================================== Feedback ================================================================
    feed = Tk()
    feed.title("Send Feedback or Report Problem")
    feed.wm_iconbitmap("logo.ico")
    feed.geometry("1315x650")
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


def about():
    a = Tk()
    a.geometry("1327x442")
    a.title("About")
    a.wm_iconbitmap("logo.ico")
    a.resizable(width=False, height=False)

    # ===========================================================================================================
    Label(a, text="About Aryan Account Sign In Wizard", bg="Dark Grey", fg="Blue", font=("Poor Richard", 62, "bold"),
          borderwidth=25, relief=RIDGE).pack(fill=X)

    Frame2 = Frame(a, borderwidth=20, bg="Dark Green", relief=RAISED)
    Frame2.pack(fil=X)

    Label(Frame2, text="Created by 'Application Aryan Official Ltd'""\n Version 5.0"
                       "\n All Copyrights reserved""\n If you want to see about license and further help."
                       " Kindly visit our official website""\n 'www.application.aryan.official.com'", bg="Dark Green",
          fg="White", font=("Century Gothic", 25, "bold")).pack()

    Button(a, text="Exit", bg="Dark Blue", fg="White", font=("Eras Bold ITC", 22, "bold"), borderwidth=10,
           relief=RAISED, command=a.destroy).pack(anchor="ne")

    a.mainloop()


def Exit():
    b = tkmsbx.askyesno("Exit", "Are you sure you want to exit?")
    if b > 0:
        root.destroy()

# =========================================================== Main GUI ===========================================

if __name__ == '__main__':
    root = Tk()
    root.title("Aryan Account Sign In")
    root.geometry("1199x600+100+50")
    root.resizable(0, 0)
    root.iconbitmap("./logo.ico")

# ========================================= MenuBar==========================================================
    Menubar = Menu(root)
    m1 = Menu(Menubar, tearoff=0, bg="Light Grey", font=("Eras Bold ITC", 11))
    m1.add_command(label="Help", command=Help)
    m1.add_command(label="Send Feedback or Report Problem", command=feedback)
    m1.add_separator()
    m1.add_command(label="About", command=about)
    m1.add_command(label="Exit", command=Exit)
    Menubar.add_cascade(label="More", menu=m1)

    root.config(menu=Menubar)

# =========================================================== Background image ==========================
    bg = ImageTk.PhotoImage(file="./background image.jpg")
    Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

# ========================================== Frames and Labels ======================================= 
    f1 = Frame(root, bg="White")
    f1.place(x=150, y=150, height=280, width=950)

    title = Label(root, text="Welcome to Application Aryan Official", font=("Poor Richard",50, "bold"), fg="Blue", bg="Dark Grey",
                bd=20, relief=RIDGE)
    title.pack(fill=X)

    title = Label(f1, text="Login Here", font="Impact 50 bold ", fg="#d77337", bg="White")
    title.grid(row=0, column=0)

    aryan_id = Label(f1, text="Write your Aryan ID:", font=("Century Gothic", 20, "bold"), bd=10, bg="Powder blue", fg="Red", relief=SUNKEN)
    aryan_id.grid(row=1, column=0)

    pass_label = Label(f1, text="Write your password:", font=("Century Gothic", 20, "bold"), bd=10, bg="Powder blue", fg="Red", relief=SUNKEN)
    pass_label.grid(row=2, column=0)

# ========================================================= buttons ===============================================
    forgot_pass = Button(f1, text="Forgot Password", font=("consolas", 20, "bold"), fg="Green", bd=0, bg="White",
                         command=for_pass, cursor="hand2")
    forgot_pass.grid(row=3, column=0)

    # forgot_id = Button(f1, text="Forgot Aryan Id", font=("consolas", 20, "bold"), fg="Green", bd=0, bg="White", 
    #                     command=for_id, cursor="hand2")
    # forgot_id.grid(row=4, column=0)
    
# ======================================= Entries =======================================================
    aryanVar = StringVar()
    passVar = StringVar()

    Aryan_Entry = Entry(f1, text="aryanVar", font="Arial 20 bold", bd=10, relief=RAISED, width=41)
    Aryan_Entry.grid(row=1, column=1)

    pass_Entry = Entry(f1, text="passVar", font="Arial 20 bold", bd=10, relief=RAISED, width=41)
    pass_Entry.grid(row=2, column=1)


    Button(root, text="Sign In", font=("Eras bold ITC", 20, "bold"), bd=15, 
            bg="Dark Green", fg="White", command=sign).pack(side=BOTTOM, anchor="se")

    root.mainloop()
