import math

dataFile = open('day12/data.txt', 'r')
data = []
for x in dataFile:
    x.split()
    data.append(x.split()[0])

boatX = 0
boatY = 0
wayX = 10
wayY = 1

def calcRotation(deg):
    global wayX
    global wayY
    newX = ((wayX*math.cos(math.radians(deg))) + (wayY*math.sin(math.radians(deg))))
    newY = (-1*(wayX*math.sin(math.radians(deg))) + (wayY*math.cos(math.radians(deg))))

    wayX = int(round(newX))
    wayY = int(round(newY))

def rotateWayPoint(dir, deg):
    if(dir == 'R'):
        calcRotation(deg)
    elif(dir == 'L'):
        calcRotation(-deg)


def moveNorth(num):
    global wayY
    wayY += num

def moveSouth(num):
    global wayY
    wayY -= num

def moveWest(num):
    global wayX
    wayX -= num

def moveEast(num):
    global wayX
    wayX += num

def moveForward(num):
    global boatX
    global boatY
    global wayY
    global wayX
    boatX += num * wayX
    boatY += num * wayY
    

for intruction in data:
    command = intruction[0]
    num = int(intruction[1:])

    if(command == 'N'):
        moveNorth(num)
    elif(command == 'S'):
        moveSouth(num)
    elif(command == 'E'):
        moveEast(num)
    elif(command == 'W'):
        moveWest(num)
    elif(command == 'R' or command == 'L'):
        rotateWayPoint(command, num)
    elif(command == 'F'):
        moveForward(num)
    


#get the manhattan distance
print('The Manhattan Distance: ' + str(abs(boatX) +  abs(boatY)))

