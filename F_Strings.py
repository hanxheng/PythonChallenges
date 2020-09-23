#23/9/2020

number = 17


def binaryConvert():
    numList = []
    again = 'Y'
    b = "Binary"
    x = "Hexadecimal"
    d = "Denary"

    while again == 'Y':
        number = int(input('Enter number: '))
        numList.append(number)
        again = input('Enter again? (Y/N): ')
        
 
    print(f"{b:<15}{x:<15}{d:<15}")
    for number in numList:
        numB = f"{number:b}"
        numX = f"{number:x}"
        numD = f"{number:d}"

        print(f"{numB:<15}{numX:<15}{numD:<15}")

binaryConvert()
