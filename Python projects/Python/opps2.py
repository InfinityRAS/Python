print("This is a students' class program using OOP in Python")

class Students:
    def __init__(self, name, classAndSection, admissionNumber):
        self.studentName = name
        self.studentClassAndSection = classAndSection
        self.studentAdmissionNumber = admissionNumber

    def getDetails(self):
        print(f"Name of Student: {self.studentName} \nClass and Section of the Student: {self.studentClassAndSection} "
              f"\nAdmission Number of the Student is: {self.studentAdmissionNumber} ")

    def updateDetails(self, newName, newClassAndSection):
        self.studentName = newName
        self.studentClassAndSection = newClassAndSection

    def listen(self):
        print("Hello World")


# Make students' class variable like that Adm(admissionNumber) = students(arguments)
a = input("Do you want to register student? (y/n): ")
if a == 'y':
    name = input("Student's name: ")
    classAndSection = input("Students' class and section: ")
    admNum = input("Student's admission Number: ")
    name = Students(name, classAndSection, admNum)
    print(name)
    print("--------------------------------------------------------")
    print(name.studentName)
    print(name.studentClassAndSection)
    print(name.studentAdmissionNumber)

else :
    print("Thanks!")

