# =============================starting===========================================================================


def greet_sign_up():
    e = input("Write your name:")
    print("Hello!")
    print("Welcome", e, "to Application Aryan Official", "\n",
          "Here you can create an Aryan Account to use various apps created by Application Aryan Official",
          "\n", "So, Let's get started!")


greet_sign_up()


def end():
    print("Thanks for Choosing Application Aryan Official")
    print("-------------------------------------------------------------")
    input()
    return


# =====================================sign up===================================================================
def sign_up():
    global q, x, y
    q = input("Write your User Name:")
    print("NOTE: Please ensure that your e-mail ID should end with '@aryan.com'")
    print("otherwise your account will not be considered as Aryan Account and your account will be deleted soon")
    x = input("Write your email ID:")
    print("'", x, "'", "has been registered as Aryan ID")
    y = input("Write your password:")
    i = input("Write your password again:")
    if y == i:
        print("Both passwords are same", "\n", "Your password"
                                               " has been successfully created")
        print("By created this an Aryan Account for '", x, "' you are agreeing our terms and conditions")
        print("Now, you have to enter your Date of Birth")
        print("NOTE: Please ensure that you should be older than 13 years otherwise your "
              "account will be deactivated soon and you will get an email regards this")
        print("Kindly note the correct format to write your Date of Birth otherwise your account will not be created,"
              " It will just show that your account has been created")
        print("DD MM YYYY")
        int(input('Enter your Date of Birth:'))
        print("Congratulation! Your account has been successfully created")

# =================================Activation====================================================
        j = input("Now, finally write your password to activate your account:")
        if j == y:
            print("Correct password")
            print("Your Account has been successfully activated")
            print("Now, you can enjoy our services by signing in to devices")
            print("Thanks for Choosing Application Aryan Official")
            print("-------------------------------------------------------------")

        else:
            print("Can't activate your account", "\n", "Try activating your account later")
            end()
            return

    else:
        print("Both passwords are not same")
        print("Can't create your password")
        end()
        return


sign_up()


# ===========================starting=============================================================================
def greet_sign_in():
    print("Hello!")
    print("Welcome to Application Aryan Official", "\n", "Here you can sign in to use various features", "\n",
          "So, Let's get started!")


greet_sign_in()


# ==========================sign in===============================================================================
def sign_in():
    global q, x, y
    b = input("Write your Aryan ID:")
    if b == x:
        print("Valid Aryan ID")
        print("Welcome", q)

    else:
        print("Invalid Aryan ID")
        print("Try Signing in Later")
        end()
        return

    c = input("Write your password:")
    if c == y:
        print("Correct password")

    else:
        print("Invalid password")
        end()
        return

    d = input("Write your password again, for activating purpose:")

    if c == d:
        print("Both passwords are same")
        print("Your account has been successfully activated")

    else:
        print("Both passwords are not same", "\n", "Can't activate your account")
        print("Try signing in later")
        end()
        return

    print("A security code has send to '", b, "'")
    e = input("Write the security here:")
    if e == 'a99b88c77':
        print("Correct Security Code", "\n", "You have successfully signed in")

    else:
        print("Incorrect Security code")
        print("Try signing in later")

    end()
    return


sign_in()
