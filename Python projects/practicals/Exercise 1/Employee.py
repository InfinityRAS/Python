import time
import json

class Employee:
    def __init__(self, name, work, rank):
        self.name = name
        self.work = work
        self.rank = rank

class Display:
    commands = ["add", "list"]

    def start(self):
        global command, originalCommand
        originalCommand = input("Enter the Command >>> ")
        command = originalCommand.replace(" ", "")
        if command == "exit":
            print("Thanks for choosing application aryan official")
            time.sleep(1)
            exit()
        elif command == "":
            self.start()
        else:
            return True 

    def error(self, error):
        print("Invalid command: " + error)
        self.start()

    def add(self):
        try:
            print("Here you can add Employees")
            employeeName = input("Enter the Name of the Employee > ")
            employeeRank = input("Enter the Rank of the Employee > ")
            employeeWork = input("Enter the Work of the Employee > ")
            if not employeeName or not employeeRank or not employeeWork:
                print("All fields are required!")
                return False
            
            employee = Employee(employeeName, employeeWork, employeeRank)
            empDict = {
                'name': employee.name,
                'work': employee.work,
                'rank': employee.rank,
            }
            # print(type(empDict))
            with open("employee.txt", "a") as emp:
                emp.write(empDict + "\n")
                emp.close()
            print("Employee has been successfully added!")
        except KeyboardInterrupt:
            print("Keyboard intrupption...")
            self.add()

    def list(self):
        print("All the Employees")
        with open("employee.txt", "r") as emp:
            for i in emp.readlines():
                empStr = json.loads(i.replace("\n", ""))

                print(empStr.name)
                print(empStr.rank)
                print(empStr.work)
                # print(dict(empStr))

            emp.close()

    def execute(self):
        global command, originalCommand
        for i in self.commands:
            if i == command:        
                eval("self." + i + "()") # eval(f"self.{i}()")
                if display.start():
                    display.execute()
        else:
            self.error(originalCommand)


if __name__ == "__main__":
    display = Display()
    while True:
        if display.start():
            display.execute()
            