"""
You have to create a program to find whether a given year is leap or not 
You can create a function for this also
Give answer in comment section and solution will be discussed in next class
"""

# Solution of the above exercise is given below


def leapOrNot():
    try:
        year = int(input("Enter the year to be checked: "))
        if year % 4 == 0:
            print("the year is the leap year")

        else:
            print("the given year isn't the leap year")

    except Exception as e:
        print(f"Some error occurred: {e}")
        leapOrNot()


leapOrNot()
input()
