import math

# ======================================= Starting==================================


def greet():
    a = input("Write your name:")
    print("Hello", a, "\n", "Welcome to Application Aryan Official")


def end():
    print("Thanks for choosing Application Aryan Official")
    input()


greet()
x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))


# ==================================== All Functions ====================================


def add(b, c):
    d = b + c
    print("Answer:", d)


def sub(b, c):
    e = b - c
    print("Answer:", e)


def mul(b, c):
    f = b * c
    print("Answer:", f)


def div(b, c):
    g = b / c
    print("Answer:", g)


def int_div(b, c):
    h = b // c
    print("Answer:", h)


def mod(b, c):
    i = b % c
    print("Answer:", i)


def rt_sqr(b, c):
    j = math.sqrt(b)
    k = math.sqrt(c)
    print("Square root of", b, "is:", j)
    print("Square root of", c, "is:", k)


def exp(b, c):
    m = pow(b, c)
    print(b, "raised to the power", c, "is:", m)


# ====================================== Calculator =========================================
def calc():
    print("Please use the following operators:", "\n", "+ and - for Addition and Subtraction", "\n",
          "* and / for Multiplication and Division", "\n", "// to Divide the number and get output in integer form",
          "\n",
          "** for exponent", "\n", "√ to find square root of a number (press Alt + 251 to get this symbol)", "\n",
          "% to divide the number and get the remainder")

    n = input("Enter the operator:")

    if n == '+':
        add(x, y)

    elif n == '-':
        sub(x, y)

    elif n == '*':
        mul(x, y)

    elif n == '/':
        div(x, y)

    elif n == '//':
        int_div(x, y)

    elif n == '%':
        mod(x, y)

    elif n == '**':
        exp(x, y)

    elif n == '√':
        rt_sqr(x, y)

    else:
        print("Invalid Operator ")


calc()
end()
