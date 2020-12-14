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
iteration = 0
found = False

print('Beginning Stamp: ' + str(beginStamp))
print(buses)
print(busesArr)
addNum = []

for i in range(len(buses)):
    if(buses[i].isdigit()):
        addNum.append(i)

print(addNum)




        



        




