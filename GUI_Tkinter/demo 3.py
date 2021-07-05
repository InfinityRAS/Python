from tkinter import *
root = Tk()

root.geometry("1366x700")
root.title("About Periodic Table")
root.wm_iconbitmap("logo.ico")


title_label = Label(text="The periodic table, also known as the periodic table of elements,"
                         "\n is a tabular display of the chemical elements, which are arranged by atomic number, "
                         "\n electron configuration, and recurring chemical "
                         "\n properties. The structure of the table shows periodic trends."
                         "\n The seven rows of the table, called periods,"
                         "\n generally have metals on the left and nonmetals on the right. The columns, "
                         "\n called groups, contain elements with similar chemical behaviours. S"
                         "\n ix groups have accepted names as well as assigned numbers: "
                         "\n for example, group 17 elements are the halogens; and group 18 are the noble gases."
                         "\n Also displayed are four simple rectangular areas or blocks associated with the filling"
                         "\n f different atomic orbitals.", bg="Dark Grey", fg="Red", padx=113, pady=9,
                    font=("Century Gothic",19, "bold"), borderwidth=10, relief=SUNKEN)

title_label.pack(side=BOTTOM,anchor="sw", fill=X)

aryan_label = Label(text="Welcome to Application Aryan Official", bg="Powder Blue",fg="Blue",
                    font=("Poor Richard",60,"bold"), borderwidth=50, relief=SUNKEN)

aryan_label.pack(anchor="ne",fill=X)

root.mainloop()
