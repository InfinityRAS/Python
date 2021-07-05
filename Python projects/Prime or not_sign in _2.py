# ====================================== starting ==================================================
def greet():
    a = input("Write your name:")
    print("Hello", a, "\n", "Welcome to Application Aryan Official,"
                            " Here you can find whether a given number is Prime or not")


def end():
    print("Thanks for choosing Application Aryan Official")
    input()


greet()

# =============================== Sign in  ======================================================


def sign_in_calc():
    print("You need to sign in to find whether a given number is Prime or not")
    b = input("Write your Aryan ID:")

# ================================ Aryan ID ====================================================
    if b == 'aryan.sisodiya1306987@aryan.com':
        print("Valid Aryan ID")
        c = input("Write your password:")

# =================================== Password ==================================================
        if c == 'raj.sis.aryan':
            print("Correct password")
            print("A security code has send to 'aryan.sisodiya1306987@aryan.com'")

# ================================== Verification ===============================================
            d = input("Write the security code here:")
            if d == 'a9b8c7d6':
                print("Correct security code")
                print("You have successfully signed in")
                print("Now you can find whether a number is Prime or composite")
                print("--------------------------------------------------------------------------")
# ====================================== prime or composite =====================================
                e = int(input("Write a number to be checked whether:"))

                if e > 1:
                    for i in range(2, e):
                        if e % i == 0:
                            print("The given number is composite")
                            end()
                            input()
                            break

                    else:
                        print("The given number is Prime")
                        end()
                        input()

                if e == 1:
                    print("The given number is neither composite nor prime")
                    end()
                    input()

                if e < 1:
                    print("Can't Define")
                    end()
                    input()

# =========================== Other Else statements ==============================================
            else:
                print("Wrong security code")
                print("Try signing in later")
                end()
                return

        else:
            print("Wrong password")
            print("Try signing in later")
            end()
            return

    else:
        print("Invalid Aryan ID")
        print("Try signing in later")
        end()
        return


sign_in_calc()
end()
