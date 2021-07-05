global c, i, z, b, j, k


def end():
    print("Thanks for choosing Application Aryan Official")
    print("-------------------------------------------------------------")
    input()


# =============================================Starting===================================================
def starting():
    print('Hello, Welcome to Application Aryan Official')
    a = str(input('Please write your name:'))
    print('Welcome', a, 'to Application Aryan official')
    print('Here you can create an Aryan Account to use various apps for free created by Application Aryan Official')
    print("So, let's get started")


starting()


# =============================================sign up==================================================


def sign_up():
    global c, i, j, k, b, z
    z = str(input("Enter your User Name:"))
    print("NOTE:Please ensure that your Aryan ID should end with '@aryan.com' "
          "otherwise your account will not be considered")
    print("as Aryan Account and your account will be deleted soon")
    i = input('Write your E-mail Id:')
    print('NOTE: The e-mail you have provided will be your Aryan Id')
    b = str(input("Please Create a password:"))
    c = input("Please re-enter password:")

    if b == c:
        print('Both passwords are same', '\n', 'Now you can go to next step')
        print('Your password has been successfully created')
    else:
        print('Password you have entered again is not same as the password you have create')
        print("Try creating account later")
        end()
        return

    print("NOTE:By creating a Aryan Account for '", i, "' You agree our Terms and Conditions")
    print("Now, you have to enter your Date of Birth")

    print("NOTE: Please ensure that you should be older than 13 years otherwise your "
          "account will be deactivated soon and you will get an email regards this")

    print("Kindly note the correct format to write your Date of Birth otherwise your account will not be created,"
          " It will just show that your account has been created")
    print("DD MM YYYY")
    input('enter your Date of Birth:')
    print("Congratulation! Your account has been successfully created")


# ===================================================activation==========================================


def activate():
    d = input("Now, finally write your password to activate your account:")

    if d == c:
        print("Congratulation! Your account has been successfully Activated")
        print("Now you can enjoy our services by signing in to devices")
    else:
        print("Sorry! that's a wrong password", "\n", "Try activating your account later")
        end()
        return

    print("Thanks for Choosing Application Aryan Official!")
    print("----------------------------------------------------------------")


sign_up()
activate()


# =======================================sign in================================================
def sign_in():
    global j, k
    print("Welcome to our Sign In page")
    h = input("Enter your Aryan id:")

    if h == i:
        print("Valid Aryan ID", "\n", "Hello,", z, "\n", "Now enter your password")
    else:
        print("Invalid Aryan ID")
        print("Try signing in later")
        end()
        return

    j = input("Write your password:")
    k = input("Write your password again, for activating purpose:")


sign_in()


# ======================================password and activation=======================================


def pass_act():
    if b == j:
        print("Correct password")
    else:
        print("wrong password")
        print("Try signing in later")
        end()
        return

    if j == k:
        print("Congratulation! Your account has been successfully Activated")
    else:
        print("Activation failed due to entered wrong password second time", "\n", "try Signing in later")
        end()
        return


pass_act()


# =======================================verification using security code=================================


def verify():
    print("A security code has send to '", i, "'")
    lm = input("Write security code here:")
    m = str("130612")

    if lm == m:
        print("Correct Security Code")
        print("You have Successfully signed in")
        end()
        return
    else:
        print("Wrong security code", "\n", "Try to sign in later")
        end()
        return


verify()
