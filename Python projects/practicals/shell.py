
def greet():
    print("Welcome to AAO's shell")
    print("")
    print("Copyright (c) 2021 Application Aryan Official. All Rights Reserved")

def error(command):
    print("Invalid command:", command)
    start()

def functionName():
    global name, Originalname
    Originalname = input("Enter a command>>> ")
    name = Originalname.replace(" ", "").lower()

    if name == "":
        functionName()
        func()

    elif name == "exit":
        print("Thanks for using this shell")
        exit()

    else:
        return True

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

def func():
    global name, Originalname
    functions = ["add", "show", "delete", "about", "list"]

    for funcs in functions:
        if name == funcs:
            eval(funcs + "()")
            start()
            return ""

    else:
        error(Originalname)

def start():
    value = functionName()
    if value:
        func()

if __name__ == "__main__":
    greet()
    start()