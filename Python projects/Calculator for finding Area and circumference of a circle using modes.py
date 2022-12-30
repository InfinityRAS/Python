# =============================starting=================================================
print("Hello!")
b = input("Please write your name:")
print("Welcome", b, "to Application Aryan Official", "\n", "Here you can find the circumference of a circle in just 2 "
                                                           "seconds!", "\n",
      "You have to just enter the radius of the circle"
      )
print("NOTE: By using Quick answer mode you can't find area of a Circle. "
      "If you want to find thee area of the circle too, Please use Premium Mode")
print("NOTE: If you don't have Aryan ID, Please use Quick answer mode or Create an Account")


def end():
    print("Thanks for choosing Application Aryan Official")
    print("-------------------------------------------------------------")
    input()
    return


# =================================calculator=============================================
def calc():
    j = str(input("Which mode do you want to use: Premium mode or Quick answer mode:"))
    k = "Premium mode"
    p = "Quick answer mode"
    if j == k:
        print("Please Sign in")
        z = str("aryan.sisodiya1306987@aryan.com")
        y = input("Please enter your Aryan ID:")

        if y == z:
            print("Valid Aryan ID")
        else:
            print("Invalid Aryan ID")
            end()

        x = input("Please enter your Password:")
        if x == 'raj.sis.aryan':
            print("Valid Password")
        else:
            print("Invalid password")
            end()

        print("You have successfully signed in")
        d = int(input("Write the radius of the circle (in cm):"))
        e = 22 / 7
        f = 2
        c = e * f
        print("The circumference of the circle is (in cm):", d * c)
        print("We hope that you have got your answer")
        print("Thanks for choosing Application Aryan Official")
        print("-----------------------------------------------------------")
        print("Hello")
        print("Welcome", b, "to Application Aryan Official", "\n",
              "Here you can find the area of a circle in just 2 seconds",
              "\n", "You have to just enter the radius of the circle")
        j = int(input("Please write the radius of the circle:"))
        print("Area of the circle is:", (j ** 2) * e)
        print("We hope that you have got your answer")
                 
    elif j == p:
        d = int(input("Write the radius of the circle (in cm):"))
        e = 22 / 7
        f = 2
        c = e * f
        print("The circumference of the circle is (in cm):", d * c)
        print("We hope that you have got your answer")

    else:
        print("Please answer in either 'Premium mode' or 'Quick answer mode'")
        calc()

# ====================================end====================================================


calc()
end()
