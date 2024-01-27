# to find the avg of given numbers seperated by a whitespace

def findAvg (intNumList):
    return sum(intNumList)/len(intNumList)

def convertIntList (strList):
    try:
        intList = []

        for i in strList:
            intList.append(int(i))

        return intList
    
    except:
        return "Error!"

nums = str(input("Enter all the numbers seperated by a whitespace: "))

numsList = list(nums.split(" "))
# print(numsList, convertIntList(numsList))
print(f"The average of the given numbers is: {findAvg(convertIntList(numsList))}")

