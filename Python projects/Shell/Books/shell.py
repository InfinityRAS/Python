import time

def greet():
    """
    An Books app that i made through the basic python... 
    Hello Coders!,
        This project is not complete yet!... I've made this a shell where you can execute the commands that are valid, my second attempt to made a app like this..!, basically a books manager shel... that is a shell, you can add the books by using the commands
        as i said earlier that this project isn't complete yet!, but i try this project to complete as soon as possible... I shall also try to make a GUI of this!, using Tkinter.. but later on!... any contributions are always Welcome 🙂🙂🙂🙂🙂🙂🙂🙂🙂
    """

    print("Application Aryan Official books Shell\nCopyright (c) 2021 Application Aryan Official. All rights reserved\n")

def functionName() :
    global funcNameOriginal, funcName
    try:
        funcNameOriginal = str(input("AAOS Enter a Command> "))

        funcName = funcNameOriginal.replace(" ", "")

        if funcName == "":
            functionName()
            func()

        elif funcName == "exit":
            print("")
            print("Thanks for using this shell")
            print("")
            time.sleep(1.5)
            exit()
        else:
            return True

    except KeyboardInterrupt:
        print("Keyboard intrruption.. Please enter the command again\n")
        funcNameOriginal = str(input("AAOS Enter a Command> "))

        funcName = funcNameOriginal.replace(" ", "")

        if funcName == "":
            functionName()
            func()

        elif funcName == "exit":
            print("")
            print("Thanks for using this shell")
            print("")
            exit()
        else:
            return True


def error(commandName):
    print("Invalid Command:", commandName)
    start()

def func():
    global funcName, funcNameOriginal, functions

    functions = ["add", "show", "delete", "list", "about"]
    for funcs in functions:
        if funcName == funcs:
            eval(funcs + "()")
            start()
            return ""

    else:
        error(funcNameOriginal)

class Book :
    def __init__(self, issuer, name, author, type, date) :
        self.issuer = issuer
        self.name = name
        self.author = author
        self.type = type
        self.date = date

    def getDetails(self):
        dict = {
            "issuer": self.issuer,
            "name": self.name,
            "author": self.author,
            "type": self.type,
            "date": self.date
        }

        return dict

    def getList(self):
        arr = [self.issuer, self.name, self.author, self.type, self.date]
        return arr

def add():
    try:
        global book
        issuerI = input("Enter the name of the issuer: ")
        nameI  = input("Enter the name of the book: ")
        authorI = input("Enter the name of the author: ")
        typeI = input("Enter the type of book issued: ")
        dateI = input("Date of issue: ")

        if issuerI != "" and nameI != "" and authorI != "" and typeI != "" and dateI != "" :
            book = Book(issuerI, nameI, authorI, typeI, dateI)
            list = book.getDetails()
            with open(".\shell.txt", "a") as shell:
                print(list)
                shell.write(f"{list}\n")
                shell.close()

            return True

        else:
            print("All fields are required!")
            return False

    except KeyboardInterrupt:
        print("KeyboardInterruption... Please enter the command again..\n")
        global books
        issuerI = input("Enter the name of the issuer: ")
        nameI  = input("Enter the name of the book: ")
        authorI = input("Enter the name of the author: ")
        typeI = input("Enter the type of book issued: ")
        dateI = input("Date of issue: ")

        if issuerI != "" and nameI != "" and authorI != "" and typeI != "" and dateI != "" :
            books = Book(issuerI, nameI, authorI, typeI, dateI)
            list = books.getDetails()
            with open(".\shell.txt", "a") as shell:
                print(list)
                shell.write(f"{list}\n")
                shell.close()

            return True
        else:
            print("All fields are required!")
            return False
        

def delete():
    pass
       
def list():
    global functions
    print("The list of the valid commands are given below:")
    for i in functions:
        print(i)

def show():
    with open("shell.txt", "r") as shell:
    # print(shell.readlines())
        print("All your Books are:")
        for todos in shell.readlines():
            strTodo = todos.replace("\n", "")
            print(strTodo)
            shell.close()


def about():
    print("Application Aryan Official Book's Shell is a task automation,\nconfiguration management framework from Application Aryan Official,\nconsisting of a command-line shell \nInitially a Application Aryan Official App's component only, known as Application Aryan Official Shell\nit was made open-source and cross-platform on July 28, 2021 \nwith the introduction of Application Aryan Official Book's Shell Core\nIt is formally made using the Python.\nVersion: 3.0.0")

def start():
    value = functionName()
    if value:
        func()

if __name__ == "__main__":
    greet()
    start()

