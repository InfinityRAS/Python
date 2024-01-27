string = input("Enter the brackets to be checked: ")

arr = []
checkDic = {
    ')': '(',
    '}': '{',
    ']': '['
}

for i in string:
    if i in ['(', '{', '[']:
        arr.append(i) # an array of all opened brackets that i will later use to check its closing bracket is there and written consecutively

    else:
        if arr[-1] == checkDic[i]:
            arr.pop(-1) # the bracket got its closing backet

        else:
            pass # wtf should i write?

print(arr)
if len(arr) == 0: print("balanced")
else: print("unbalanced")


