##2/9/2020
##ISBN


myNumber = input('Please enter your 10 digit ISBN10 number ')
myList = []
numberList = [10,9,8,7,6,5,4,3,2]
totalList = []
result = 0
remainder = 0

for x in range(9):
    myList.append(int(myNumber[x]))
    
for z in range(9):
    totalList.append(myList[z] * numberList[z])
for a in totalList:
    result += a

result = result % 11
result = 11 - result

if result == int(myNumber[9]):
    print('yes')




    




    
