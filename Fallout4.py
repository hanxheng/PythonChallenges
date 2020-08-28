##28/8/2020
##Fallout  4 hacking terminal
import random
import string
import time

myList = ["TAKES",
          "KNOWN",
          "KICKS",
          "STARK",
          "BOOTS",
          "BATON",
          "CLEAR",
          "CRIME",
          "WASTE",
          "CLOSE",
          "SWORD",
          "SLAVE",
          "FARGO",
          "MAYBE",
          "MALES"]

def checkLike(string1, string2):
    likeness = 0
    for x in range(5):
        if string1[x] == string2[x]:
            likeness += 1
    return likeness

def printBoard():
    global myList
    characters = string.punctuation

    for x in range(0, len(myList) - 2, 2):
        line = ''.join(random.choice(characters) for i in range(4))
        line2 = ''.join(random.choice(characters) for i in range(4))
        print(line + ' ' + myList[x] + ' ' + line2 + ' ' + myList[x + 1])

def winScreen():
    print('''
Welcome to ROBCO Industries (TM) Termlink
Museu












>Password accepted''')
        
def start():
    attemptsLeft = 4
    password = myList[random.randint(0, len(myList) - 1)]
    guess = None
    access = False
    
    print('''
Welcome to ROBCO Industries (TM) Termlink

Password Required''')

    printBoard()

    while attemptsLeft != 0:
        guess = input(">Enter password ")

        if guess != password:
            print(">" + guess)
            print(">Entry denied")
            print(">Likenesss=" + str(checkLike(guess, password)))
            attemptsLeft -= 1
            print(">Attempts remaining: " + str(attemptsLeft))

        elif guess == password:
            winScreen()
            attemptsLeft = 0
            access = True
    return access


while True:
    access = start()
    if access:
        exit()
    else:
        for x in range(5):
            print('''
    Welcome to ROBCO Industries (TM) Termlink

    Password Required





    LOCKED OUT  - TIME REMAINING : ''' + str(5 - x))
            time.sleep(1)
            
        
        
        
            
