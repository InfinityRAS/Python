# to remove the duplicates from the given array

arr = input("Enter the elements of the list seperated by a space: ").split(" ")

print(arr)

modifiedArr = []

for i in arr:
    if i in modifiedArr:
        pass

    else:
        modifiedArr.append(i)

print(modifiedArr)
