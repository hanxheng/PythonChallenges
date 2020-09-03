##4/9/2020
##Make it laugh string

import string

vowels = ['a','e','i','o','u']
myString = input('Enter string: ')
def make_it_laugh(myString):
    for x in vowels:
        myString = myString.replace(x, 'haha')
    print(myString)
make_it_laugh(myString)
    
