dataFile = open('day15/data.txt', 'r')
data = []
for x in dataFile:
    data = x.split(',')
dataFile.close()

dataInt = []
for x in data:
    dataInt.append(int(x))   

#pairs values with indexs
dataIndexes = []
for i in range(len(dataInt)):
    dataIndexes.append(i)


print(dataInt)
print(dataIndexes)

#This needs to return the last index of the called number
def findLastDiff(currIndex,findNum):
    global dataIndexes
    global dataInt
    secIndex = dataIndexes[dataInt.index(findNum)]
    return currIndex - secIndex 


    
   


initLength = len(dataInt)
for i in range(30000000-len(dataInt)):
    currentI = initLength + i
    #Was the last number called in the array
    if(dataInt.count(dataInt[-1]) > 1):
        num = dataInt[-1]
        #returns number of turns away from the other number
        dataInt.append(findLastDiff(currentI-1,dataInt[-1]))
        dataIndexes.append(currentI)

        #Delete the last index
        delIndex = dataInt.index(num)
        del dataInt[delIndex]
        del dataIndexes[delIndex]

    else:
        dataInt.append(0)
        dataIndexes.append(currentI)


print(dataInt[-1])