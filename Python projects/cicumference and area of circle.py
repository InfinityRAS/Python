# =======================starting========================================================

f = input("Write your Name:")


def greet():
    print("Hello", f, "\n", "Welcome to Application Aryan Official", "\n",
          "Here you can find the area or circumference of the circle in just 2 seconds")


greet()

u = int(input("Enter the radius of the circle:"))
e = input("What do you want to find; Area or Circumference of Circle (a or c):")


# =======================functions==========================================================


def circum(a):
    b = a * 22 / 7 * 2
    print("Circumference:", b)


def area(a):
    d = a ** 2 * 22 / 7
    print("Area:", d)


def end():
    print("Thanks for choosing Application Aryan Official")
    print("------------------------------------------------------------------------------")
    input()
    return


# ==============================calculator===================================================


def calc():
    if e == 'a':
        area(u)
        i = input("Do you want to find the circumference of circle too?: ")
        if i == 'yes':
            b = float(input("Enter the radius of the circle:"))
            circum(b)

        else:
            end()
            return

    elif e == 'c':
        circum(u)
        j = input("Do you want to find the area of the circle too?: ")
        if j == 'yes':
            z = float(input("Enter the radius of the circle:"))
            area(z)

        else:
            end()
            return

    else:
        print("Please answer in 'c' or 'a'")
        g = input("What do you want to find; Area or Circumference of Circle (a or c):")
        if f == 'a':
            area(u)
            i = input("Do you want to find the circumference of circle too?: ")
            if i == 'yes':
                b = float(input("Enter the radius of the circle:"))
                circum(b)
        elif g == 'c':
            circum(u)
            j = input("Do you want to find the area of the circle too?: ")
            if j == 'yes':
                z = float(input("Enter the radius of the circle:"))
                area(z)
        else:
            print("Please answer in 'c' or 'a'")
            g = input("What do you want to find; Area or Circumference of Circle (a or c):")
            if g == 'a':
                area(u)
                i = input("Do you want to find the circumference of circle too?: ")
                if i == 'yes':
                    d = float(input("Enter the radius of the circle:"))
                    circum(d)
            elif g == 'c':
                circum(u)
                j = input("Do you want to find the area of the circle too?: ")
                if j == 'yes':
                    z = float(input("Enter the radius of the circle:"))
                    area(z)
            else:
                print("Please answer in 'c' or 'a'")
                h = input("It is the last chance, What do you want to find; Area or Circumference of Circle (a or c):")
                if h == 'a':
                    area(u)
                    i = input("Do you want to find the circumference of circle too?: ")
                    if i == 'yes':
                        x = float(input("Enter the radius of the circle:"))
                        circum(x)
                elif h == 'c':
                    circum(u)
                    j = input("Do you want to find the area of the circle too?: ")
                    if j == 'yes':
                        z = float(input("Enter the radius of the circle:"))
                        area(z)
                else:
                    return


calc()
end()
