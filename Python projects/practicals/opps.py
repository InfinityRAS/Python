print("this is tutorial on OOPS")

class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def printDetails(self):
        return f"Name is {self.name}, Role is {self.role}, salary is {self.salary} "

    def changeDetails(self, newName, newRole, newSalary):
        self.name = newName
        self.role = newRole
        self.salary = newSalary


aryan = Employee("Aryan", "Dangerous Programmer", 2)
aryan.changeDetails("Aryan sisodiya", "Web Developer", 250)
print(aryan.printDetails())