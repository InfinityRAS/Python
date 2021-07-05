from tkinter import *


# ========================================== functions =====================================
def my_name():
    print("My name is Aryan Sisodiya")


def father_name():
    print("My father's name is Mr. Ashok Kumar")


def mother_name():
    print("My mother's name is Mrs. Rajni Singh")


def bro_name():
    print("My brother's name is Aditya Sisodiya")


def school_name():
    print("My school's name is Ashok Memorial Public School")


# ===========================================Frames and Labels ======================================
root = Tk()

root.wm_iconbitmap("logo.ico")
root.title("Buttons Demo")
root.geometry("1164x606")
root.minsize(811, 524)

f1 = Frame(root, bg="Dark Grey", borderwidth=20, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, bg="Dark Grey", borderwidth=15, relief=RAISED)
f2.pack(side=TOP, anchor="ne", fill="x")

a = Label(f1, text="Aryan Sisodiya", font=("Century Gothic", 20, "bold"))
a.pack(pady=143)

b = Label(f2, text="Welcome to Application Aryan Official", font=("Century Gothic", 20, "bold"), bg="Dark Grey",
          fg="White")
b.pack()

frame = Frame(root, borderwidth=20, bg="Light Grey", relief=SUNKEN)
frame.pack(side=BOTTOM, anchor="s")

aryan = PhotoImage(file="3.png")
Label(image=aryan, borderwidth=10, relief=SUNKEN).pack(anchor="nw")

# ================================= Buttons ===============================================================
b1 = Button(frame, text="What is your name?", fg="White", font=("Century Gothic", 20, "bold"), bg="Blue",
            command=my_name)
b1.pack(pady=10)

b2 = Button(frame, text="What is your Father's name?", fg="White", font=("Century Gothic", 20, "bold"), bg="Red",
            command=father_name)
b2.pack(pady=10)

b3 = Button(frame, text="What is your Mother's name?", fg="White", font=("Century Gothic", 20, "bold"),
            bg="Red",
            command=mother_name)
b3.pack(pady=10)

b4 = Button(frame, text="What is your Brother's name?", fg="White", font=("Century Gothic", 20, "bold"),
            bg="Red",
            command=bro_name)
b4.pack(pady=10)

b5 = Button(frame, text="What is your School's name?", fg="White", font=("Century Gothic", 20, "bold"),
            bg="Red",
            command=school_name)
b5.pack(pady=10)

Button(f1, text="Exit", bg="Dark Green", font=("Eras Bold ITC", 25, "bold"), command=root.destroy, relief=RAISED,
       borderwidth=15, fg="White").pack(side=BOTTOM, fill=X)

root.mainloop()
