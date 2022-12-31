import sys
import time
import json

def printInfo ():
    print("Application Aryan Official Shell for adding Employees\nCopyright (c) 2023-2024 Application Aryan Official. All rights reserved\n")

def showError(error):
    print("Invalid Command:", error)
    start()

def add():
    try:
        name = str(input("Enter the Name of the Employee: "))
        rank = str(input("Enter the Rank of the Employee: "))
        work = str(input("Enter the Work of the Employee: "))

        if not name or not rank or not work:
            print("All fields are required")
            add()

        else:
            empDict = {
                'name': name,
                'work': work,
                'rank': rank,
            }

            with open("./employee.txt", "a") as emp:
                emp.write(json.dumps(empDict) + "\n")
                # emp.write(empDict + "\n")
                
                emp.close()

            print("Employee has been successfully added!")
    except KeyboardInterrupt:
        print("Keyboard Interruption... Enter the data again")
        add()

def help():
    global allValidCommands
    print("The list of the valid commands are given below:")
    for i in allValidCommands:
        print(i)

def show():
    print("All your Employees are:")
    allEmp = []

    with open("./employee.txt", "r") as f:
        for i in f.readlines():
            # if i == "":
            #     print("No employee added till now")
            #     break
            print(i.replace("\n", ""))
            list.append(allEmp, i)

        f.close()
    
    print(allEmp)
    for i in allEmp:
        if not i:
            print("No employee added till now, execute 'add' to add one")

def delete():
    pass

def about():
        print("Application Aryan Official Shell is a task automation,\nconfiguration management framework from Application Aryan Official,\nconsisting of a command-line shell \nInitially a Application Aryan Official App's component only, known as Application Aryan Official Shell\nit was made open-source and cross-platform on December 31, 2022 \nwith the introduction of Application Aryan Official Shell Core\nIt is formally made using the Python.\nVersion: 3.0.0")

def functionName():
    try:
        global command

        originalCommand = str(input("Enter the command: "))
        command = originalCommand.replace(" ", "")

        if not command:
            functionName()
            func()

        elif command == "exit":
            print("\nThanks for using the AAO shell")
            time.sleep(1.5)
            sys.exit()

        else:
            return True
    
    except KeyboardInterrupt:
        print("\nKeyboard Interruption catached... Please enter the command again")
        functionName()

def func():
    global command, allValidCommands

    allValidCommands = ["add", "help", "about", "show", "delete"]
    if (command in allValidCommands):
        eval(command + "()")
        start()
        return True

    else:
        showError(command)

def start():
    value = functionName()
    if value:
        func()

if __name__ == "__main__":
    printInfo()
    start()
