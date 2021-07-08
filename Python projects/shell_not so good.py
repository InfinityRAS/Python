print("Hello, Welcome!")

def add():
    print("add func fired!")

def show():
    print("show func fired!")

def delete():
    print("delete func fired!")

def about():
    print("about func fired!")

def list():
    print("list func fired!")

def exit():
    print("Thanks for using this shell")

def funcN():
    global funcName, funcNameOriginal
    funcNameOriginal = input("Enter a command>>> ")
    funcName = funcNameOriginal.replace(" ", "")

    if funcName == "":
        funcN()

    elif funcName == "exit":
        return True

def error(command):
    print("Invalid command: ", command)


functions = ["add", "show", "delete", "list", "about", "exit"]
funcN()

def func():
    global funcName
    for func in functions:
        # print(func)
        if func == funcName:
            print(func)
            eval(func + "()")
            return True

        else:
            print(func)
            return False

def Check():
    if name == True:
        funcN()
        func()
        Check()

    else:
        error(funcNameOriginal)
        funcN()
        func()
        Check()

if funcN():
    exit()

else:
    name = func()



    
Check()

# name()
print("out of loop")

