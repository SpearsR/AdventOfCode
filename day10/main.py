dataFile = open('day10/testdata.txt', 'r')
data = []
for x in dataFile:
    data.append(int(x))

data.sort()
print(data)
print(max(data))

deviceJolts = max(data) + 3
onJolt = 0
atEnd = False
oneDiff = 0
twoDiff = 0
threeDiff = 0

while not atEnd:
    can1, can2, can3 = False, False, False


    #This counts all possible jumps
    if(data.count(onJolt + 3) == 1 or (onJolt + 3) == max(data) + 3):
        threeDiff += 1
        can3 = True
    if(data.count(onJolt + 2) == 1):
        twoDiff += 1
        can2 = True
        if(can3):
            oneDiff += 1
    if(data.count(onJolt + 1) == 1):
        oneDiff += 1
        can1 = True
        if(can3):
            twoDiff += 1
        if(can2):
            oneDiff += 2
            if(can3):
                oneDiff += 1

    #jump based on conditions
    if(can1):
        onJolt += 1
    elif(can2):
        onJolt += 2
    else:
        onJolt += 3

    print("onJolt: " + str(onJolt) +  " oneDiff: " + str(oneDiff) + " twoDiff: " + str(twoDiff) + " threeDiff: " + str(threeDiff))

    if(onJolt == max(data)+3):
        atEnd = True


data.sort()
print(data)



 
    

    


    
    






