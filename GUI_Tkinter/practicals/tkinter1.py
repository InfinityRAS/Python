from tkinter import *

root = Tk()

root.title("Hello world!")
label1 = Label(text="Hello world", bg="Dark Grey", fg="Red", padx=113, pady=9, font=("Century Gothic",19, "bold"),
               borderwidth=10)
label1.pack(side=TOP, anchor="n", fill=X)

root.mainloop()
