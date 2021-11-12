 def func():
    print("Hello")
    print("Welcome to Application Aryan Official")
    print("Please Sign In to use Calculator")
    f = str(input("Enter your Aryan ID:"))
    g = str("aryan.sisodiya1306987@aryan.com")
    if f == g:
        print("Valid Aryan ID")
    else:
        print("Invalid User Id")
        print("Try signing in Later")
    h = str(input("Enter your Password:"))
    i = str("raj.sis.aryan")
    if h == i:
        print("Correct password")
        print("You have successfully signed in")
    else:
        print("Invalid Password")
        print("Try signing in Later")
    print("----------------------------------------------------------------------------------------")

while True:
    func()
