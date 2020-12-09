dataFile = open("data.txt", "r")
data = []
for x in dataFile:
    data.append(x.split())

dataFile.close()

#Split List into Chars
def getCharList(str):
    return[char for char in str]

sepData = []
for slope in data:
    sepData.append(getCharList(slope[0]))

#Setting Varibles
yPos = 0
xPos = 0
hitTreeCount = 0
xPosChange = int(input('Right: '))
yPosChange = int(input('Down: '))
lengthArr = len(sepData)
notAtBottom = True
iterations = int(len(sepData) / yPosChange)

while yPos < len(sepData):
    for i in range(iterations - 1):
        xPos += xPosChange
        yPos += yPosChange
        if(xPos <= 30 and yPos < lengthArr):
            if(sepData[yPos][xPos] == '#'):
                hitTreeCount += 1
        elif(xPos > 30 and yPos < lengthArr):
            xPos -= 31
            if(sepData[yPos][xPos] == '#'):
                hitTreeCount += 1
        

print('Trees Hit: ' + str(hitTreeCount))




