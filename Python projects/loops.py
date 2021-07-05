# Loops in Python 
""" What are loops?
Loops are also called as Iterative statements

for loop and while loop """

# for Loop
# Syntax of for loop
""" 
for (variable) in range():
    statements
"""

# Example 1
""" 
nos = [4, 6, 10, 45, "harry", "Aryan", "Kanha", "Aditya", "I am a good boy"]
for i in nos:
    print(i) 
"""

""" 
range() function
range function will create a list of the numbers from the first argument(integer) to the predecessor of second argument(integer) and it will create a list  in which the diffrernce between each number will be the third argument(inetger), by default it is 1.

Example:
range(a, b, c)  # This will create a list of number from a to b-1.
"""

# Example 2
""" 
for i in range(0, 11, 2):
    print(i)
"""

# Example 3
""" 
firstnum = int(input('Write the starting number: '))
secondnum = int(input('Write the ending number: '))

if firstnum % 2 == 0:
    for i in range(firstnum, secondnum + 1, 2):
        print("Even numbers between",firstnum, "and", secondnum, "is", i)

else:
    for i in range(firstnum, secondnum + 1, 2):
        print("Odd numbers between",firstnum, "and", secondnum, "is", i)
"""

# While loop
# while loop syntax
""" 
intialisation
while condition:
    statements
    updation
"""

# Example 1
""" 
i = 0
while i <= 10:
    print(i)
    i += 1 # Updating the value of i: i + 1
"""

# Infinite Loop
# Example 1
""" 
i = 5
while i > 4:
    print(i)
    i += 1
"""

# Example 2
""" 
i = 0
while i < 5:
    print(i)
"""    