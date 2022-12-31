employeeArray = []
name = input("Write Employee's name: ")
experience = input("Write his/her experience: ")
salary = input("Write his/her salary: ")

employeeList = [name, experience, salary]
register = input("Do you want to register? (Y/N): ")

if register == 'Y':
    employeeArray.append(employeeList)
    print("Registered Successfully")
else:
    print("Can't Register")

print(employeeArray)
