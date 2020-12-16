dataFile = open('day15/data.txt', 'r')
data = []
for x in dataFile:
    data = x.split(',')
dataFile.close()

dataInt = []
for x in data:
    dataInt.append(int(x))   
print(dataInt)

#This needs to return the last index of the called number
def findLastDiff(cur,findNum):
    global dataInt
    iteration = len(dataInt)
    count = -1
    for num in dataInt:
        iteration -= 1
        if(dataInt[iteration] == findNum):
            count += 1
        if(count >= 1):
            prevIndex = iteration
            break
    
    return cur - prevIndex


initLength = len(dataInt)
for i in range(30000000-len(dataInt)):
    currentI = initLength + i - 1
    #Was the last number called in the array
    if(dataInt.count(dataInt[-1]) > 1):
        #returns number of turns away from the other number
        dataInt.append(findLastDiff(currentI,dataInt[-1]))
    else:
        dataInt.append(0)

print(dataInt[-1])