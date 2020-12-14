dataFile = open('day13/testdata.txt', 'r')
data = []
for x in dataFile:
    data.append(x.split()[0])

dataFile.close()
busesArr = []
buses = data[1].split(',')


def getBuses():
    for item in buses:
        if(item.isdigit()):
            busesArr.append(int(item))
getBuses()


busesCon = []
for item in buses:
    busesCon.append(item)


#This gets the count for variable minutes
spaceForMinutes = []
allArr = data[1].split(',')
start = 0
for b in range(len(allArr)):
    if(allArr[b].isdigit()):
        spaceForMinutes.append(allArr[start:b].count('x'))
        start = b

beginStamp = 0
upBy = 1
waitingArr = []
def firstOcc(mult,to): 
    waiting = True
    iteration = 0
    while waiting:
        beginStamp = mult * iteration
        if(beginStamp%busesArr[0] == 0 and beginStamp != 0):
            sub  = True
            nextUp = beginStamp
            for i in range(len(busesArr[:to])): #17, 13   0,1
                for x in range(spaceForMinutes[i]+1):
                    if((nextUp+x)%busesArr[i] != 0):
                        sub = False
                    else:
                        sub = True
                        nextUp += x
                        break
                nextUp += 1
                
            if(sub):
                waiting =False
                break
        iteration += 1
    return  beginStamp





upBy = firstOcc(upBy,1)
upBy = firstOcc(upBy,2)
upBy = firstOcc(upBy,3)
print(upBy)

        




