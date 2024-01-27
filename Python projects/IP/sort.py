numList = [-6, -100, 0, -9, 6, 5]
sortedlist = []

def minima(myList):
    assumedMin = myList[0] # lets assume the first one is minimum

    for i in myList:
        if assumedMin > i: assumedMin = i
        else: continue

    return assumedMin

def sort(argList):
    if len(argList) != 0:
        sortedlist.append(minima(argList))
        argList.remove(minima(argList))

        if len(argList) != 0:
            sort(argList)

        else:
            return sortedlist

sort(numList)

print(sortedlist)

