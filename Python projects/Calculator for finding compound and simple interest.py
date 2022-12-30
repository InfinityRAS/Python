print("Hello!")
j = str(input("Write your name:"))
print("Welcome", j, "to Application Aryan Official", "\n", "Here you can find the compound interest in just 2 seconds",
      "\n",
      "You've to just enter the data in the following")
a = float(input("Enter the principle amount (in Rs.):"))
b = float(input("Enter the Rate of Interest (in %):"))
c = float(input("Enter the time (in years):"))
d = 100
e = d + b
f = e / d
g = f ** c
h = g * a
i = h - a
print("Compound interest is:", i)
print("And Amount is:", h)
print("We hope that you have get your answer")
print("-----------------------------------------------------------------------------------------------")
m = str(input("Do you want to find the simple interest also? (Please Answer in 'yes' or 'no'):"))
if m == 'yes':
    print("Hello!")
    print("Welcome", j, "to Application Aryan Official", "\n",
          "Here you can find the simple interest in just 2 seconds",
          "\n", "You've to just enter the data in the following")
    n = int(input("Enter the principle amount (in Rs.):"))
    o = int(input("Enter the Rate of Interest (in %):"))
    p = int(input("Enter the time (in years):"))
    q = n * o * p
    r = q / d
    s = r + n
    print("Simple interest is:", r)
    print("And Amount is:", s)
    print("We hope that you have get your answer")
    print("Thanks for Choosing Application Aryan Official")
else:
    print("Thanks for Choosing Application Aryan Official")
print("-----------------------------------------------------------------------------------------------")
input()
