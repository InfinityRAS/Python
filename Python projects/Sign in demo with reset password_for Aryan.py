global d, q, n, a
print('Welcome to Application Aryan Official', '\n', 'Please sign in')
c = str(input('write your Aryan ID:'))
o = str("aryan.sisodiya989898@aryan.com")


def sign_in():
    global o, d, q, n
    z = str('aryan')
    if c == o:
        print("Valid Aryan ID")
        x = input('Please Write your password:')
    else:
        print("Invalid Aryan Id")
        print("Try signing in later")
        input()
        return
    if x == z:
        print('Welcome Aryan Sisodiya', '\n', 'You have successfully signed in')
    else:
        print('Wrong password', '\n', 'Please enter it again')
        b = input('Write your Password:')
        if b == z:
            print('Welcome Aryan Sisodiya', '\n', 'You have successfully signed in')
        else:
            print('wrong password')
            print(
                "It is last chance. If you enter a wrong password again, Your account access will be temporarily "
                "blocked")
            d = input('Write your password:')
            if d == z:
                print('Welcome Aryan Sisodiya', '\n', 'You have successfully signed in')
            else:
                print('Wrong password', '\n', 'Your account access has been temporarily blocked')
    print("You are going to Reset your password",
          "\n", "NOTE: If you do not want to reset your password,Just Enter any security code")

    # =======================verification================================================================
    print('a Security code has sent to your email')
    p = '999666'
    m = input('Enter code here:')
    global q, n
    if m == p:
        print("Correct Security Code")
        q = str(input("enter your new password here:"))
        n = str(input("Re-enter your password:"))

        if q == n:
            print("Your password has successfully changed")
        else:
            print("Both passwords are not same", "\n", "Try resetting your password later")

    else:
        print('wrong security code, try resetting your password later')


sign_in()
print('Thanks for Choosing Application Aryan official')
