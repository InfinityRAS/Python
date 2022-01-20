import string
import random

if __name__ == '__main__':
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    punc = string.punctuation

    passlen = int(input("enter the length of the password: "))
    liststr = []

    liststr.extend(list(lower))
    liststr.extend(list(upper))
    liststr.extend(list(digit))
    liststr.extend(list(punc))

    # print(liststr)
    password = random.sample(liststr, passlen)
    print("your password is:", "".join(password))
    input()