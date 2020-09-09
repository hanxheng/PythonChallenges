#6/9/2020
#Poker hands


numOrder = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
cardOrder = [
    '2D', '2C', '2H', '2S',
    '3D', '3C', '3H', '3S',
    '4D', '4C', '4H', '4S',
    '5D', '5C', '5H', '5S',
    '6D', '6C', '6H', '6S',
    '7D', '7C', '7H', '7S',
    '8D', '8C', '8H', '8S',
    '9D', '9C', '9H', '9S',
    'TD', 'TC', 'TH', 'TS',
    'JD', 'JC', 'JH', 'JS',
    'QD', 'QC', 'QH', 'QS',
    'KD', 'KC', 'KH', 'KS',
    'AD', 'AC', 'AH', 'AS']
suitOrder = ['D', 'C', 'H', 'S']

myFile = open('poker.txt', 'r')
myString = myFile.readline() #reads first line
myList = [] # list of all played cards
for a in myFile:
    myList.append(a)
myFile.close()

def splitToCards(myString):
    p1List = []
    p2List = []

    myString = myString.replace(' ', '')
    for x in range(0, len(myString) - 1, 2):
        if x < len(myString)/2 - 1:
            p1List.append(myString[x] + myString[x + 1])
        else:
            p2List.append(myString[x] + myString[x + 1])
    return p1List, p2List


def arrangeCards(myList):
    newList = []
    orderList = []

    for y in myList:
        orderList.append(cardOrder.index(y))
    orderList.sort()

    for z in orderList:
        newList.append(cardOrder[z])
    return newList

def getOrder(myList):
    newList = []
    
    for x in myList:
        newList.append(numOrder.index(x[0]))

    return newList

def findStraight(myList):
    orderList = getOrder(myList)
    count = 0
    
    for x in range(len(orderList) - 1):
        if orderList[x + 1] == orderList[x] + 1 :
            count += 1
    if count == 4:
        return True, myList[4][0]
    else:
        return False, myList[4][0]

def findFlush(myList):
    count = 0
    for x in range(len(myList) - 1):
        if myList[x][1] == myList[x + 1][1]:
            count += 1
    if count == 4:
        return True, myList[0][1]
    else:
        return False, None

def findFOAK(myList):
    count = 0
    FOAKVal = None
    
    for x in range(4):
        if myList[x][0] == myList[x + 1][0]:
            count += 1
        elif myList[x][0] != myList[x + 1][0] and count != 3:
            count = 0
            
        if count == 3:
            FOAKVal = myList[x][0]
    if count == 3:
        return True, FOAKVal
    else:
        return False, FOAKVal

def findHouse(myList):
    tempList = []
    pairList = []
    tripList = []
    pairCount = 0
    tripCount = 0
    tripVal = None
    
    pair = False
    trip = False

    for z in myList:
        tempList.append(z)

    for x in range(4):
        if x == 0:
            if tempList[x][0] == tempList[x + 1][0] and tempList[x][0] != tempList[x + 2][0]:
                pairCount += 1
        if x > 0 and x < len(tempList) - 2:
            if tempList[x][0] == tempList[x + 1][0] and tempList[x][0] != tempList[x + 2][0] and tempList[x][0] != tempList[x - 1][0]:
                pairCount += 1
        if x == len(tempList) - 2:
            if tempList[x][0] == tempList[x + 1][0] and tempList[x][0] != tempList[x - 1][0]:
                pairCount += 1
            
        if pairCount == 1:
            tempList.remove(tempList[x])
            tempList.remove(tempList[x])
            break
        
    for y in range(2):
        if tempList[y][0] == tempList[y + 1][0]:
            tripCount += 1
        if tripCount == 2:
            tripVal = tempList[y][0]
            
            break

    if tripCount + pairCount == 3:
        return True, tripVal
    else:
        return False, None

def findTrip(myList):
    tempList = []
    tripVal = None
    trip = False

    for y in myList:
        tempList.append(y)

    for x in range(3):
        if tempList[x][0] == tempList[x + 1][0] == tempList[x + 2][0]:
            trip = True
            tripVal = tempList[x][0]
            tempList.remove(tempList[x])
            tempList.remove(tempList[x])
            tempList.remove(tempList[x])
            break

    if trip and tempList[0][0] != tempList[1][0]:
        return True, tripVal
    else:
        return False, tripVal

def findPair(myList):
    tempList = []
    pairCount = 0
    val1 = None
    val2 = None
    pairVal = None
    house = False

    for z in myList:
        tempList.append(z)

    for x in range(len(tempList) - 1):
        if tempList[x][0] == tempList[x + 1][0]:
            val1 = tempList[x][0]
            pairCount += 1
            tempList.remove(tempList[x])
            tempList.remove(tempList[x])
            pairVal = val1
            break

    for y in range(len(tempList) - 1):
        if tempList[y][0] == tempList[y + 1][0]:
            val2 = tempList[y][0]
            pairCount += 1
            if numOrder.index(pairVal) < numOrder.index(tempList[y][0]):
                pairVal = tempList[y][0]
            tempList.remove(tempList[y])
            tempList.remove(tempList[y])
            break

    if tempList[0][0] == val1 or tempList[0][0] == val2 or val1 == val2:
        house = True
    
    if pairCount == 2 and house == False:
        return True, pairVal, pairCount
    else:
        return False, pairVal, pairCount

def findStraightFlush(straight, flush, myList):
    straightFlush = False
    royalFlush = False
    straightFlushVal = None
    
    if straight and flush:
        straightFlush = True
    if straight and flush and myList[0][0] == 'T':
        royalFlush = True
    straightFlushVal = myList[4]
    return straightFlush, royalFlush, straightFlushVal 

#returns the value 0 - 9 representing highcard to royal flush
def checkCombo(myList):

    #missing a 2 3 4 5
    #straightVal is the digit in the straight
    straight, straightVal = findStraight(myList)

    #flushVal is the suit of the list
    flush, flushVal = findFlush(myList)

    #FOAKVal is the digit of the card that occured 4 times
    FOAK, FOAKVal = findFOAK(myList)

    #houseVal is the digit in which the card is repeated 3 times
    house, houseVal = findHouse(myList)

    #tripVal is the digit in which the card is repeated 3 times
    trip, tripVal = findTrip(myList)

    #pairVal is the highest digit that is a pair
    #if pair is true and pairCount = 2 two pairs
    #if pair is false and pairCount = 1 one pair
    #if pair is false and pairCount = 2 4oak or house
    pair, pairVal, pairCount = findPair(myList)

    #highest card
    highCard = myList[4]

    #straight flush and royal, straightFlushVal is the highest card
    straightFlush, royalFlush, straightFlushVal = findStraightFlush(straight, flush, myList)

    if royalFlush:
        return 10, straightFlushVal
    elif straightFlush:
        return 9, straightFlushVal
    elif FOAK:
        return 8, FOAKVal
    elif house:
        return 7, houseVal
    elif flush:
        return 6, flushVal
    elif straight:
        return 5, straightVal
    elif trip:
        return 4, tripVal
    elif pair and pairCount == 2:
        return 3, pairVal
    elif pair == False and pairCount == 1:
        return 2, pairVal
    else:
        return 1, highCard

#returns True if p1 wins and False if p2 wins.
def compare(p1Val, p1CardVal, p2Val, p2CardVal, p1High, p2High):
    if p1Val > p2Val:
        return True
    elif p2Val > p1Val:
        return False
    elif p2Val == p1Val:
        if p1Val == 10 or p1Val == 9:
            if cardOrder.index(p1CardVal) > cardOrder.index(p2CardVal):
                return True
            elif cardOrder.index(p1CardVal) < cardOrder.index(p2CardVal):
                return False
        if p1Val == 8 or p1Val == 7 or p1Val == 5 or p1Val == 4 or p1Val == 3 or p1Val == 2:
            if numOrder.index(p1CardVal) > numOrder.index(p2CardVal):
                return True
            elif numOrder.index(p2CardVal) > numOrder.index(p1CardVal):
                return False
        if p1Val == 6:
            if suitOrder.index(p1CardVal) > suitOrder.index(p2CardVal):
                return True
            elif suitOrder.index(p2CardVal) > suitOrder.index(p1CardVal):
                return False

        #high card
        if p1CardVal == p2CardVal or p1Val == 1:
            if cardOrder.index(p1High) > cardOrder.index(p2High):
                return True
            elif cardOrder.index(p2High) > cardOrder.index(p1High):
                return False




def main(myList):
    p1Wins = 0
    for x in myList:
        p1List, p2List = splitToCards(x)
        p1List = arrangeCards(p1List)
        p2List = arrangeCards(p2List)

        p1High = p1List[4]
        p2High = p2List[4]

        p1Val, p1CardVal = checkCombo(p1List)
        p2Val, p2CardVal = checkCombo(p2List)

        p1Win = compare(p1Val, p1CardVal, p2Val, p2CardVal, p1High, p2High)
        if p1Win:
            p1Wins += 1

    print(p1Wins)

main(myList)


    
    




