import math


def loop():                     # we are defining a function using 'def' keyword
    # the function that this function will do starts from here {
    a = int(input("Enter starting number:"))
    b = int(input("Enter ending number:"))
    c = int(input("What should be the power?:"))

    if a < b:
        while a <= b:
            print(math.pow(a, c))
            a += 1

    else:
        while a >= b:
            print(math.pow(a, c)) # = math.pow(a, c) = a**c
            a -= 1

    input()

    # } The function ends here


loop()                      # We are calling the function to do the function assigned in it
loop()                      # We can call a function thousand times to avoid writing the same large code thousand times
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()
loop()

# the above code is equal to the code given below
i = 1
while i <= 26:
    loop()
    i += 1
