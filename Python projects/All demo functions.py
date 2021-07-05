from math import sqrt

a = int(input("Enter a number:"))
b = int(input("Enter the second number:"))


def rt_sqr(x, y):
    d = sqrt(x)
    c = sqrt(y)
    print("Square root of", x, "is:", d)
    print("Square root of", y, "is:", c)


def exp(x, y):
    c = pow(x, y)
    print(x, "raised to the power", y, "is:", c)


def pi(x, y):
    d = x * 22 / 7
    e = y * 22 / 7
    print(x, "times of pi is:", d)
    print(y, "times of pi is:", e)


rt_sqr(a, b)
exp(a, b)
pi(a, b)
print("-----------------------------------------------------------------------------------")

# =====================even and odd numbers============================================
a = int(input("Enter a starting number:"))
b = int(input("Enter a ending number:"))

if a < b:
    if a % 2 != 0:
        print("Even numbers between these two numbers are:")

        for i in range(a + 1, b, 2):
            print(i)

        else:
            print("Odd numbers between these two numbers is:")
            for p in range(a + 2, b, 2):
                print(p)

    if a % 2 == 0:
        print("Even numbers between these two numbers are:")
        for z in range(a + 2, b, 2):
            print(z)

        else:
            print("Odd numbers between these two numbers is:")
            for m in range(a + 1, b, 2):
                print(m)

if a > b:
    if a % 2 != 0:
        print("Even numbers between these two numbers are:")

        for i in range(a - 1, b, -2):
            print(i)

        else:
            print("Odd numbers between these two numbers is:")
            for p in range(a - 2, b, -2):
                print(p)

    if a % 2 == 0:
        print("Even numbers between these two numbers are:")
        for z in range(a - 2, b, -2):
            print(z)

        else:
            print("Odd numbers between these two numbers is:")
            for m in range(a - 1, b, -2):
                print(m)

input()
