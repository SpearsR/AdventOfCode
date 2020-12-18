from itertools import product

fileName = 'day17/data.txt'
dataFile = open(fileName, 'r')
data = []
for x in dataFile:
    data.append(list(x[:-1]))
dataFile.close()

#Array of tuples for checking close blocks
neighbor_tuple = list(product(range(-1,2), repeat=3))
neighbor_tuple.remove((0,0,0))


#Now we need a function that converts the input data into cordinates
blocks_cords = []
convert_data = data[:]
yPos = len(data)
for iteration in range(len(data)):
    yPos -= 1
    for xPos in range(len(data[iteration])):
        if(data[iteration][xPos] == '#'):
            blocks_cords.append([(xPos,yPos,0), True])
        else:
            blocks_cords.append([(xPos,yPos,0), False])
            
yPos = len(data)
for iteration in range(len(data)):
    yPos -= 1
    for xPos in range(len(data[iteration])):
            blocks_cords.append([(xPos,yPos,1), False])
            blocks_cords.append([(xPos,yPos,-1), False])


def applyRules(blocks):
    newBlocks = []

    activeCords = []
    neighbor_active = []
    switch_to_active = set()
    #Add all the active cords to array
    for i in range(len(blocks)):
        if(blocks[i][1]):
            activeCords.append(blocks[i][0])
            #Add all neighbor cords to array
            for next in neighbor_tuple:
                active_block = blocks[i][0]
                newX = active_block[0] + next[0]
                newY = active_block[1] + next[1]
                newZ = active_block[2] + next[2]
                neighbor_active.append((newX,newY,newZ))
            
    for block in activeCords:
        if(shouldActiveStay(activeCords,block)):
            newBlocks.append([block, True])

    #Sees if inactives could be active
    for common in neighbor_active:
        if(neighbor_active.count(common) == 3):
            switch_to_active.add(common)
    for common in switch_to_active:
        newBlocks.append([common, True])

    return newBlocks

#Returns True is the block should stay active
def shouldActiveStay(actives, cords):
    global neighbor_tuple
    count = 0
    for next in neighbor_tuple:
        newX = cords[0] + next[0]
        newY = cords[1] + next[1]
        newZ = cords[2] + next[2]
        if(actives.count((newX,newY,newZ)) > 0):
            count += 1
    if(count == 3 or count == 2):
        return True
    else:
        return False


count = 0
testArr = blocks_cords[:]
for i in range(6):
    testArr = applyRules(testArr)
    for item in testArr:
        if(item[1]):
            count += 1

print(count)