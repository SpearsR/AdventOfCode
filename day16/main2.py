dataFile = open('day16/data.txt', 'r')
data = []
for x in dataFile:
    data.append(x)
dataFile.close()

ranges = []
for x in range(20):
    temp = data[x].split(': ')[1][:-1]
    temp1, temp2 = temp.split(' or ')
    ranges.append(temp1.split('-'))
    ranges.append(temp2.split('-'))

def isInRange(num):
    global ranges
    inRange = False
    for range in ranges:
        if(num >= int(range[0]) and num <= int(range[1])):
            inRange = True
            break
    return inRange

myticket = data[22][:-1].split(',')

#Gather test data
testdata = []
newData = data[25:]
inValid = []
valid_tickets = []


#Returns valid tickets
for ticket in newData:
    ticket = ticket[:-1].split(',')
    ticketValid = True
    for num in ticket:
        if(not isInRange(int(num))):
            inValid.append(int(num))
            ticketValid = False
    if(ticketValid):
        valid_tickets.append(ticket)


rangesWithCols = []
dataDict = []
for iteration in range(20):
    range1 = ranges[0 + iteration*2]
    range2 = ranges[1 + iteration*2]
    rangeSet = []
    for i in range(len(myticket)):
        fitsRange = True    
        for b in range(len(valid_tickets)):
            number = int(valid_tickets[b][i])
            if( (number >= int(range1[0]) and number <= int(range1[1])) or (number >= int(range2[0]) and number <= int(range2[1])) ):
                continue
            else:
                fitsRange = False
                break
        if(fitsRange):
            print('Range ' + str(iteration) +  ' work for column ' + str(i))
            rangesWithCols.append([iteration, i])
            rangeSet.append(i)
        print(rangeSet)
    dataDict.append([iteration, rangeSet])
print(dataDict)

rangesFinal = []
colsFinal = []

for item in dataDict:
    rangesFinal.append(item[0])
    colsFinal.append(item[1])


print(rangesFinal)
print(colsFinal)


for i in range(len(colsFinal)):
    for b in range(len(colsFinal)):
        if(len(colsFinal[b]) == 1):
            print('Range ' + str(b) + ' is for column ' + str(colsFinal[b][0]))
            removeNum = colsFinal[b][0]
            for item in colsFinal:
                try:
                    item.remove(removeNum)
                except:
                    pass
            break

print(int(myticket[1]) * int(myticket[6]) * int(myticket[19]) * int(myticket[2]) * int(myticket[16]) * int(myticket[17]))