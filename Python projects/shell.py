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

    funcNameOriginal = str(input("Enter a Command>>> "))
    funcName = funcNameOriginal.replace(" ", "")

    if funcName == "":
        functionName()
        func()

    elif funcName == "exit":
        print("Thanks for using this shell")
        exit()

    else:
        return True

def error(commandName):
    print("Invalid Command:", commandName)
    start()

def func():
    global funcName, funcNameOriginal

    functions = ["add", "show", "delete", "list", "about", "WhatIsMyName", "exit"]
    for funcs in functions:
        # print(funcs)
        if funcName == funcs:
            eval(funcs + "()")
            start()
            return ""

    else:
        error(funcNameOriginal)

def add():
    print("this is the add func")

def delete():
    print("this is the delete func")

def list():
    print("this is the list func")

def show():
    print("this is the show func")

def about():
    print("this is the about func")

def WhatIsMyName():
    print("My name is Aryan sisodiya")

def start():
    value = functionName()
    if value:
        func()

if __name__ == "__main__":
    greet()
    start()

