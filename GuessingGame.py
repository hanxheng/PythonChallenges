#21/8/2020
import random
answer = random.randint(1,100)
userAnswer = 0
while userAnswer != answer:
    try:
        userAnswer = int(input('GUESS'))
    except ValueError:
        print('Non-valid input')
        continue

    if userAnswer > answer:
        print('Too high')
    elif userAnswer < answer:
        print('Too low')
print('Correct!')
