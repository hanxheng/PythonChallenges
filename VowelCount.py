##25/8/2020

myString = input('Enter string ')
noOfVowels = 0
vowels = ['a','e','i','o','u']

for x in range(len(myString)):
    for y in range(len(vowels)):
        if myString[x] == vowels[y]:
            noOfVowels += 1
print(noOfVowels)
            
