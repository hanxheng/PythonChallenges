##2/9/2020
##random number generator

import random
myList = []

def randomList(listLength, lowBound, upBound):
    myList = []
    
    for x in range(listLength):
        myList.append(random.randint(lowBound, upBound))

    return myList
    
def calcMean(myList):
    total = 0
    mean = 0
    
    for x in myList:
        total += x

    mean = total / len(myList)

    print(mean)

def findMin(myList):
    min = myList[0]
    
    for y in myList:
        if y < min:
            min = y

    print(min)

def findMax(myList):
    max = myList[0]

    for z in myList:
        if z > max:
            max = z

    print(max)


myList = randomList(50, 0, 100)
calcMean(myList)
findMin(myList)
findMax(myList)
