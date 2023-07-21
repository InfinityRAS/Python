# finding roots of a quadratic eqn

# a,b,c = 1,-2,1

# disc = b**2 - 4*a*c
# f = -b/(2*a)
# g = disc/(2*a)

# print(disc, f, g)
# root1 = f + g
# root2 = f - g

# print(root1, root2)

# calculate factorial

# def fact(num):
#     if num == 1:
#         return 1
    
#     if num > 1:
#         return num*fact(num-1)

# print(fact(3))

# for solving a quadratic eqn by hit and trial in a given integer interval

lwrLmt = int(input("Enter the lower integer limit of interger interval: "))

uppLmt = int(input("Enter the upper integer limit of interger interval: "))

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

for i in range(lwrLmt, uppLmt):
    str = eval("a*(i**2) + b*i + c")

    if (str == 0):
        print(str, i)
        print(f"solutions: {i}")
        continue

