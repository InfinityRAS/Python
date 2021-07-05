# Solution of exercise given in previous video is given below

import math

# ============================== Greeting ========================================
def greet(): 
    name = input("Write your name: ")
    print("Hello,", name, "\n Welcome to Application Aryan Official")

greet()

# ================================== All Functions =============================

# Function for Adding two values
def add(a, b):
    print("Answer is:", int(a) + int(b))

# Function for Subtracting two values
def sub(a, b):
    print("Answer is:", int(a) - int(b))

# Function for Multiplicating two values
def mul(a, b):
    print("Answer is:", int(a) * int(b))

# Function for dividing two values and getting the exact quotient
def div(a, b):
    print("Answer is:", int(a) / int(b))

# Function for dividing two values and getting the integer quotient
def flr_div(a, b):
    print("Answer is:", int(a) // int(b))

# Function for Dividing two values and getting the remainder (modulus function)
def mod(a, b):
    print("Answer is:", int(a) % int(b))

# Function for Exponent
def exp(a, b):
    print("Answer is:", pow((int(a), int(b))))
    # print(int(a) ** int(b)) Both are correct

# Function for getting the square root of a number
def sqrt(a, b):
    print("Square root of", a, "is: ", math.sqrt(a))
    print("Square root of", b, "is: ", math.sqrt(b))

# ==================================== Main file =======================================

x = int(input("Enter a number: "))
y = int(input("Enter a second number: "))
print(
    "Please use the following operators:", "\n+ and - for Addition and Subtraction", "\n* and / for Multiplication and Division", "\n// to Divide the number and get output in integer form",
          "\n** for exponent", "\n√ to find square root of a number (press Alt + 251 to get this symbol)", "\n% to divide the number and get the remainder"
)
z = input("Enter a operator of your choise from above: ")
if z == '+':
    add(x, y)

elif z == '-':
    sub(x, y)

elif z == '*':
    mul(x, y)

elif z == '/':
    div(x, y)

elif z == '//':
    flr_div(x, y)

elif z == '%':
    mod(x, y)

elif z == '√':
    sqrt(x, y)

elif z == '**':
    sub(x, y)

else:
    print("Invalid Operator")

print("Thanks for Choosing Application Aryan Official")