##28/8/2020
##Bubble sort

myList = [1, 9, 2, 10, 23, 1, 3, 13, 90]
swaps = None

def swap(a , b):
    temp = a
    a = b
    b = temp
    return a, b

def bSort(myList):
    global swaps
    while swaps != 0:
        swaps = 1
        for x in range(len(myList) - 1):
            if myList[x] > myList[x + 1]:
                myList[x], myList[x + 1] = swap(myList[x], myList[x + 1])
                swaps += 1
        swaps -= 1
    print(myList)
    
bSort(myList)
                
    
