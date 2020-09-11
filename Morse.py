#10/9/2020
#morse code converter
charList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
morseList = [
    '. ---',
    '--- . . .',
    '--- . --- .',
    '--- . .',
    '.',
    '. . --- .',
    '--- --- .',
    '. . . .',
    '. .',
    '. --- --- ---',
    '--- . ---',
    '. --- . .',
    '--- ---',
    '--- .',
    '--- --- ---',
    '. --- --- .',
    '--- --- . ---',
    '. --- .',
    '. . .',
    '---',
    '. . ---',
    '. . . ---',
    '. --- ---',
    '--- . . ---',
    '--- . --- ---',
    '--- --- . .',
    '       '
    ]
#index of character corresponds to index of its morse code

myString = input('Enter string: ')
myString = myString.upper()
textList = myString.split(' ')
#split string into list of letters
def splitToLetters(myString):
    newList = []
    
    for x in range(len(myString)):
        newList.append(myString[x])

    return newList

def convertLettersToMorse(myList):
    newList = []
    letterIndex = 0

    for y in range(len(myList)):
        if myList[y] not in charList:
            continue
        letterIndex = charList.index(myList[y])
        newList.append(morseList[letterIndex] + " ")

    return newList

def joinLetters(myList):
    newString = None

    newString = '   '.join(myList)

    return newString
    

myList = splitToLetters(myString)
morseLetterList = convertLettersToMorse(myList)
morseWord = joinLetters(morseLetterList)
print(morseWord)

        
    


    
    
