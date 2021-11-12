import time
import sys

def greet():
    """
    An todos-list app that i tried to make through tkinter but made this todos app through the basic python... 
    Hello Coders!,
        This project is not complete yet!... I've made this a shell where you can execute the commands that are valid, my first attempt to made a app like this..! that is a shell, you can add the todos by using the commands
        as i said earlier that this project isn't complete yet!, but i try this project to complete as soon as possible... I shall also try to make a GUI of this!, using Tkinter.. but later on!... any contributions are always Welcome 🙂🙂🙂🙂🙂🙂🙂🙂🙂
    """

    print("Application Aryan Official Shell\nCopyright (c) 2021 Application Aryan Official. All rights reserved\n")

def functionName() :
    global funcNameOriginal, funcName
    try:
        funcNameOriginal = str(input("AAOS Enter a Command> "))

        funcName = funcNameOriginal.replace(" ", "")

        if funcName == "":
            functionName()
            func()

        if funcName == "":
            functionName()
            func()

        elif funcName == "exit":
            print("")
            print("Thanks for using this shell")
            print("")
            time.sleep(1.5)
            # exit()
            sys.exit()
        else:
            return True

    except KeyboardInterrupt:
        print("Keyboard intrruption.. Please enter the command again\n")
        funcNameOriginal = str(input("AAOS Enter a Command> "))

        funcName = funcNameOriginal.replace(" ", "")

        if funcName == "":
            functionName()
            func()

        if funcName == "":
            functionName()
            func()

        elif funcName == "exit":
            print("")
            print("Thanks for using this shell")
            print("")
            # exit()
            sys.exit()
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

def add():
    try:
        todo = str(input("Enter the Todo's name: "))
        # print(todo)
        with open("shell.txt", "a") as shell:
            shell.write(f"\n{todo}")
            shell.close()
    except KeyboardInterrupt:
        print("Keyboard intrruption.. Please enter the command again\n")
        todo = str(input("Enter the Todo's name: "))
        # print(todo)
        with open("shell.txt", "a") as shell:
            shell.write(f"\n{todo}")
            shell.close()

    print("Your Todo has been successfully added!")

def delete():
    try:
        show()
        delTodo = input("Which todo do you want to delete? (Write its name) ")
        with open("shell.txt", "r") as f:
            lines = f.readlines()
        with open("shell.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != delTodo:
                    f.write(line)
    except KeyboardInterrupt:
        print("Keyboard intrruption.. Please enter the command again\n")
        show()
        delTodo = input("Which todo do you want to delete? (Write its name) ")
        with open("shell.txt", "r") as f:
            lines = f.readlines()
        with open("shell.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != delTodo:
                    f.write(line)

    print("Your Todo has been successfully removed!")
       
def list():
    global functions
    print("The list of the valid commands are given below:")
    for i in functions:
        print(i)

def show():
    with open("shell.txt", "r") as shell:
    # print(shell.readlines())
        print("All your todos are:")
        for todos in shell.readlines():
            strTodo = todos.replace("\n", "")
            print(strTodo)
            shell.close()


def about():
    print("Application Aryan Official Shell is a task automation,\nconfiguration management framework from Application Aryan Official,\nconsisting of a command-line shell \nInitially a Application Aryan Official App's component only, known as Application Aryan Official Shell\nit was made open-source and cross-platform on June 7, 2021 \nwith the introduction of Application Aryan Official Shell Core\nIt is formally made using the Python.\nVersion: 3.0.0")

def start():
    value = functionName()
    if value:
        func()

if __name__ == "__main__":
    greet()
    start()

