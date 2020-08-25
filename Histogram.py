##25/8/2020
count = 1
again = "yes"
myList = []

while again == "yes":
    temp = input('Enter number ' + str(count) + " ")
    myList.append(temp)
    count += 1
    
    again = input('Would you like to enter another number? ')
    again = again.lower()

    

    
def histogram(myList):
    for x in myList:
        print("*"*int(x))

histogram(myList)
