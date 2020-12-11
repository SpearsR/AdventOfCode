dataFile = open('day11/data.txt', 'r')
data = []
for x in dataFile:
    data.append(list(x.split()[0]))

def checkCloseSeated(x,y):
    seated = 0
    nextTo = [[y,x+1], [y+1,x+1], [y+1,x], [y+1,x-1], [y,x-1], [y-1,x-1],[y-1,x],[y-1,x+1]]

    for b in range(8):
        try:
            if(nextTo[b][1] >= 0 and nextTo[b][0] >= 0):
                if(nextArr[nextTo[b][0]][nextTo[b][1]] == '#'):
                    seated+=1
        except:
            pass

    if(seated >= 4):
        return True
    else:
        return False
        #to the  right

def forEmpty(x,y):
    seated = 0
    nextTo = [[y,x+1], [y+1,x+1], [y+1,x], [y+1,x-1], [y,x-1], [y-1,x-1],[y-1,x],[y-1,x+1]]

    for b in range(8):
        try:
            if(nextTo[b][1] >= 0 and nextTo[b][0] >= 0):
                if(nextArr[nextTo[b][0]][nextTo[b][1]] == '#'):
                    seated+=1
        except:
            pass
    if(seated == 0):
        return True
    else:
        return False
        #to the  right


def siftData(data):
    newArr = []
    global count
    count = 0
    for i in range(len(data)):
        row = data[i]
        temp = []
        for seat in range(len(row)):
            symbol = row[seat]
            if(symbol == '#'):
                if(checkCloseSeated(seat,i)):
                    temp.append('L')
                    count += 1
                else:
                    temp.append('#')
            elif(symbol == 'L'):
                if(forEmpty(seat,i)):
                    temp.append('#')
                    count += 1
                else:
                    temp.append('L')
            else:
                temp.append(symbol)
            
        newArr.append(temp)
        temp = []

    for item in newArr:
        print(item)
    
    print('\n')
    return newArr

count = 0
nextArr = data[:]
stillChanging = True
while stillChanging:
    nextArr  = siftData(nextArr[:])
    if(count == 0):
        stillChanging = False


seated = 0
for row in nextArr:
    for char in row:
        if(char == '#'):
            seated += 1


print(seated)



