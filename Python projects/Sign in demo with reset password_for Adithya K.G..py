global q, n

print('Welcome to Application Aryan Official', '\n', 'Please sign in')
c = input('write your name:')
print('Welcome', c)
a = input('Please Write your password:')
z = 'adithya'
if a == z:
    print('Welcome Adithya K.G.', '\n', 'You have successfully signed in')
else:
    print('Wrong password', '\n', 'Please enter it again')
    b = input('Write your Password:')

    if b == z:
        print('Welcome Adithya K.G.', '\n', 'You have successfully signed in')

    else:
        print('wrong password', '\n', 'It is last chance. '
                                      'if you enter a wrong password again, your account access will be temporarily '
                                      'blocked')

        d = input('Write your password:')
        if d == z:
            print('Welcome Adithya K.G.', '\n', 'You have successfully signed in')
        else:
            print('Wrong password', '\n', 'Your account access has been temporarily blocked')

print('You are going to Reset your password', "\n",
      'NOTE: If you do not want to reset your password, Just Enter any security code')

print('a Security code has sent to your email')
p = '989898'
m = input('Enter code here:')
if m == p:
    print("Correct Security Code")
    q = input("enter your new password here:")
    n = input("Re-enter your password:")

    if q == n:
        print("Your password has successfully changed")
    else:
        print("Both passwords are not same", "\n", "Try resetting your password later")

else:
    print('wrong security code, try resetting your password later')

print('Thanks for Choosing Application Aryan official')
