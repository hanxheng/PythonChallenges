##28/08/2020
##Linear search

myList = [8, 2, 19, 4, 10, 4, 3, 2]

def lSearch(myList):
    
    searchItem = int(input('Enter search num '))
    found = False
    index = None
    
    for x in range(len(myList)):
        if myList[x] == searchItem:
            found = True
            index = x + 1
            break
    if found:
        print("Item is in position " + str(index))
    else:
        print("Item not in list")
        
lSearch(myList)
