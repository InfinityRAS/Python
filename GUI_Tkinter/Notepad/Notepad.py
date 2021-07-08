from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os


# ============================================ functions ===================================================
def New():
    global file
    root.title("Untitled - Notepad")
    file = None
    text_area.delete(1.0, END)


def popen_():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text Document", "*.txt")])
    if file == "":
        file = None

    else:
        root.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0, END)
        f = open(file, "r")
        text_area.insert(1.0, f.read())
        f.close()


def save():
    global file
    if file is None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All files", "*.*"),
                                                                                                 ("Text Document",
                                                                                                  "*.txt")])

        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")

    else:
        f = open(file, "w")
        f.write(text_area.get(1.0, END))
        f.close()


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def Paste():
    text_area.event_generate("<<Paste>>")


def fExit():
    ask1 = askyesno("Notepad", "Do you want to leave?")
    if ask1 > 0:
        root.destroy()


def About():
    a = Tk()
    a.geometry("1327x420")
    a.title("About")
    a.wm_iconbitmap("Notepad icon.ico")
    a.resizable(width=False, height=False)

    # ===========================================================================================================
    Label(a, text="About Notepad", bg="Dark Grey", fg="Blue", font=("Poor Richard", 62, "bold"),
          borderwidth=25, relief=RIDGE).pack(fill=X)

    Frame2 = Frame(a, borderwidth=20, bg="Dark Green", relief=RAISED)
    Frame2.pack(fill=X)

    Label(Frame2, text="Created by 'Application Aryan Official Ltd'"
                       "\n All Copyrights reserved""\n If you want to see about license and further help."
                       " Kindly visit our official website""\n 'www.applicationaryanofficial.com'", bg="Dark Green",
          fg="White", font=("Century Gothic", 25, "bold")).pack()

    Button(a, text="Exit", bg="Dark Blue", fg="White", font=("Eras Bold ITC", 22, "bold"), borderwidth=10,
           relief=RAISED, command=a.destroy).pack(anchor="ne")

    a.mainloop()


def Help():
    showinfo("Notepad", "Created by Application Aryan Official \n Kindly Visit our Official Website")


def More_Help():
    ashok = Tk()
    ashok.wm_iconbitmap("Notepad icon.ico")
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
        ask = askyesno("Send Feedback or Report Problem", "Do you want to send the feedback or problem reported?")
        if ask > 0:
            with open("Feedback(Notepad).txt", "a") as g:
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
            s.wm_iconbitmap("Notepad icon.ico")
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
    feed.wm_iconbitmap("Notepad icon.ico")
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


# ========================================= Main GUI =====================================================
if __name__ == '__main__':
    root = Tk()
    root.geometry("780x650")
    root.minsize(780, 650)
    root.iconbitmap("Notepad icon.ico")
    root.title("Untitled - Notepad")

    f1 = Frame(root)
    f1.pack(fill=BOTH)

    # ================================================ Scroll Bar ======================================
    scrollBar = Scrollbar(f1)
    scrollBar.pack(side=RIGHT, fill=Y)

    text_area = Text(f1, font=("Arial", 15), yscrollcommand=scrollBar.set, height=40)
    text_area.pack(fill=BOTH, expand=True)
    file = None

    scrollBar.config(command=text_area.yview)

    # ================================================= MenuBar 1 ====================================================
    Menubar_3 = Menu(root)

    m3 = Menu(Menubar_3, tearoff=0, bg="Light Grey", font=("Eras Bold ITC", 11))
    m3.add_command(label="New", command=New)
    m3.add_command(label="Open", command=popen_)
    m3.add_separator()
    m3.add_command(label="Save", command=save)
    m3.add_separator()
    m3.add_command(label="Exit", command=fExit)
    Menubar_3.add_cascade(label="File", menu=m3)

    # ================================================= MenuBar 2 ====================================================
    m4 = Menu(Menubar_3, tearoff=0, bg="Light Grey", font=("Eras Bold ITC", 11))
    m4.add_command(label="Cut", command=cut)
    m4.add_command(label="Copy", command=copy)
    m4.add_command(label="Paste", command=Paste)
    m4.add_separator()
    m4.add_command(label="Exit", command=fExit)
    Menubar_3.add_cascade(label="Edit", menu=m4)

    # ================================================= MenuBar 3====================================================
    m5 = Menu(Menubar_3, tearoff=0, bg="Light Grey", font=("Eras Bold ITC", 11))
    m5.add_command(label="Help", command=Help)
    m5.add_command(label="More Help", command=More_Help)
    m5.add_separator()
    m5.add_command(label="About", command=About)
    m5.add_command(label="Send Feedback or report problem", command=feedback)
    m5.add_separator()
    m5.add_command(label="Exit", command=fExit)
    Menubar_3.add_cascade(label="More", menu=m5)

    root.config(menu=Menubar_3)

    root.mainloop()
