# to find the combination of given two numbers

def fact(num):
    if num==1:
        return 1
    
    if num == 0:
        return 1

    else:
        return num*fact(num-1)

# print(fact(5))

n = int(input("Enter the total objects: "))
r = int(input("Enter the number of objects to be selected: "))

if n > 0 and r >= 0 and n >= r:
    fac = fact(n)
    combiD = fact(r)*fact(n-r)
    permD = fact(n-r)

    combi = fac/combiD
    perm = fac/permD

    print(f"The total combinations are {combi}, while total permutations are {perm}")

else:
    print("numbers should be whole numbers otherwise n >= r")
