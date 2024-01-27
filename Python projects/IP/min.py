# to find the minima of a given list

myList = input("Enter the numbers seperated by a space: ").split(" ")

def minima(myList):
    # for i in range(len(myList)):
    #     myList[i] = int(myList[i])

    assumedMin = myList[0] # lets assume the first one is minimum

    for i in myList:
        if assumedMin > i: assumedMin = i
        else: continue

    return assumedMin

