count = {'[': 0,'{': 0,'(': 0,')': 0,'}': 0,']': 0}

string = input("Enter the unbalanced parenthesis: ")
for i in string:
    count[i] += 1

newStr = ""
for i in count:
    newStr += i*count[i]

print(newStr)
