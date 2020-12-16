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

for ticket in newData:
    ticket = ticket[:-1].split(',')
    ticketValid = True
    for num in ticket:
        if(not isInRange(int(num))):
            inValid.append(int(num))
            ticketValid = False
    if(ticketValid):
        valid_tickets.append(ticket)

print(len(inValid))

total = 0
for number in inValid:
    total += number

print(total)
print(len(valid_tickets))
print(len(newData))
    
    

