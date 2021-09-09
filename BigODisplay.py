from matplotlib.pyplot import ylabel, plot, show, xlabel, title
import math

def pickType():
    return input("Enter type (L, Q, E, F): ")

def setType():
    type = pickType()
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = []
    
    if type == 'L':
        for i in x:
            y.append(math.log2(i))
    elif type == 'Q':
        for i in x:
            y.append(i**2)
    elif type == 'E':
        for i in x:
            y.append(math.e**i)
    elif type == 'F':
        for i in x:
            y.append(math.factorial(i))

    return x, y

x, y = setType()
plot(x, y, 'b')
xlabel('Inputs')
ylabel('Steps')
show()
    
