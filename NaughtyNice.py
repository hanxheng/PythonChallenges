##24/8/2020

vowel = ["a", "e", "i", "o", "u"]


other = ["ab", "cd", "pq", "xy"]

noOfNice = 0
noOfNaughty = 0

file = open("Input.txt", "r")


def check(myString):
    minVowels = False
    doubleLetter = False
    otherCheck = True
    vowelNo = 0

    global noOfNice
    global noOfNaughty
    
    ##check for aeiou
    myList = []
    myList[:0] = myString
    for x in range(len(myList)):
        for b in range(len(vowel)):
            if myList[x] == vowel[b]:
                vowelNo += 1
    if vowelNo >= 3:
        minVowels = True


    ##double check
    for y in range(len(myString)):
        if y != len(myString) - 1:
            if myString[y] == myString[y + 1]:
                doubleLetter = True


    ##check for ab cd pq xy
    for z in range(len(other)):
        if myString.find(other[z]) != -1:
            otherCheck = False

    ##print nice or naughty
    if (minVowels and doubleLetter and otherCheck):
        noOfNice += 1
    else:
        noOfNaughty += 1

for a in file:
    check(a)
    
print(noOfNice)
    
