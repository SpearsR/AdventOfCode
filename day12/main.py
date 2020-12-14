import math

dataFile = open('day12/data.txt', 'r')
data = []
for x in dataFile:
    x.split()
    data.append(x.split()[0])

boatX = 0
boatY = 0
boatDeg = 0
facing = 'E'

def normalAngle():
    global boatDeg
    if(boatDeg == 360):
        boatDeg = 0
    elif(boatDeg < 0):
        boatDeg += 360
    elif(boatDeg > 360):
        boatDeg -= 360  


def calcDeg(dir, deg):
    global boatDeg
    if(dir == 'R'):
        boatDeg -= deg
    elif(dir == 'L'):
        boatDeg += deg
    normalAngle()

def getFacing():
    global facing
    global boatDeg
    if(boatDeg == 0):
        facing = 'E'
    elif(boatDeg == 90):
        facing = 'N'
    elif(boatDeg == 180):
        facing = 'W'
    elif(boatDeg == 270):
        facing = 'S'

def moveNorth(num):
    global boatY
    boatY += num

def moveSouth(num):
    global boatY
    boatY -= num

def moveWest(num):
    global boatX
    boatX -= num

def moveEast(num):
    global boatX
    boatX += num

def moveForward(num):
    global boatX
    global boatY
    global facing
    if(facing == 'N'):
        boatY += num
    elif(facing == 'S'):
        boatY -= num
    elif(facing == 'E'):
        boatX += num
    elif(facing == 'W'):
        boatX -= num


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
        calcDeg(command, num)
        getFacing()
    elif(command == 'F'):
        moveForward(num)
    


#get the manhattan distance
print('The Manhattan Distance: ' + str(abs(boatX) +  abs(boatY)))
