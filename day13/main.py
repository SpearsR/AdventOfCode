dataFile = open('day13/data.txt', 'r')
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


busesCon = []
for item in buses:
    busesCon.append(item)

beginStamp = int(data[0])
getBuses()

waitingArr = []
waiting = True
while waiting:
    for i in range(len(busesArr)):
        if(beginStamp%busesArr[i] == 0):
            waitingArr.append(1)
            global firstId
            firstId = busesArr[i]
        else:
            waitingArr.append(0)
    
    for x in range(len(busesArr)):
        print(str(busesArr[x])+ ' ', end='')

    print('\n')

    for y in range(len(busesArr)):
        print(str(waitingArr[y])+ ' ', end='')

    print('\n')
    if(waitingArr.count(1) >= 1):
        waiting = False
    beginStamp += 1
    waitingArr = []




print(((beginStamp -1)- int(data[0])) * firstId)

print(busesCon)