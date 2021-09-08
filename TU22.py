import datetime

timeLength = 0
startTime = 0
def toggleTimer():
    global startTime
    global timeLength

    if(startTime == 0):
        startTime = datetime.datetime.now()
    else:
        timeLength = datetime.datetime.now() - startTime
        startTime = 0
    
toggleTimer()

a = input("enter text: ")

toggleTimer()
print(timeLength)