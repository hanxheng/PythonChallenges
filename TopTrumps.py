##1/9/2020
##Top trumps

import random

cardList = [
    ['Chantal', 3],
    ['Ian', 10],
    ['Kingsley', 4],
    ['Kasey', 3],
    ['Finley', 9],
    ['Mahir', 8],
    ['Ben', 1],
    ['Aayush', 6],
    ['Jonah', 7],
    ['Manal', 5],]

player1Val = None
player2Val = None

p1Hand = []
p2Hand = []

#0 = draw
#1 = p1 win
#2 = p2 win
player1Win = None


def drawHands(cardList):
    global p1Hand 
    global p2Hand
    
    for x in range(5):
        count = random.randint(0, len(cardList) - 1)
        p1Hand.append(cardList[count])
        cardList.remove(cardList[count])
        
    for x in range(5):
        count = random.randint(0, len(cardList) - 1)
        p2Hand.append(cardList[count])
        cardList.remove(cardList[count])

def p1Turn():

    print('Player 1:')
    for x in range(len(p1Hand)):
        print(str(x) + ': ' + str(p1Hand[x]).translate({ord(i): None for i in '[]'}))
            
    choice = int(input('Which card would you like to play? (0 - ' + str(len(p1Hand)) + ')'))

    p1Hand.remove(p1Hand[choice])
    player1Turn = False
    return int(p1Hand[choice][1])

def p2Turn():

    print('Player 2:')
    for y in range(len(p2Hand)):
        print(str(y) + ': ' + str(p2Hand[y]).translate({ord(i): None for i in '[]'}))
            
    choice = int(input('Which card would you like to play? (0 - ' + str(len(p2Hand)) + ')'))

    p2Hand.remove(p2Hand[choice])
    player1Turn = False
    return int(p2Hand[choice][1])


        

def compare(player1Val, player2Val):
    if player1Val > player2Val:
        #player 1 wins
        return 1
    elif player2Val > player1Val:
        #player 2 wins
        return 2
    else:
        #draw
        return 0

def main():

    p1Wins = 0
    p2Wins = 0
    
    while True:
        player1Val = p1Turn()
        player2Val = p2Turn()
        player1Win = compare(player1Val, player2Val)
        if player1Win == 1:
            print('\nPlayer1 win\n')
            p1Wins += 1
        elif player1Win == 2:
            print('\nPlayer 2 win\n')
            p2Wins += 1
        else:
            print('\nDraw\n')
        if len(p1Hand) == 0:
            if p1Wins > p2Wins:
                print('Player 1 wins the game')
            elif p2Wins > p1Wins:
                print('Player 2 wins the game')
            else:
                print('Draw')
        
drawHands(cardList)
main()


    
