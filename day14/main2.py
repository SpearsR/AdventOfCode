from itertools import permutations
from itertools import combinations
from itertools import product

dataFile = open('day14/data.txt', 'r')
data = []
for x in dataFile:
    data.append(x[:-1])
dataFile.close()

mask = ''
memValue = []
memLocation = []

def binaryToNumber(bin):
    return int(bin,2)

#Returns new mem locations in an array
def addMemMask(location):
    global mask
    binLocation = numToBinary(location)
    sep = list(binLocation)

    #This creates the new mask over the memory binary
    for b in range(len(sep)):
        bit = mask[b]
        if(bit == '1'):
            sep[b] = bit
        elif(bit == 'X'):
            sep[b] = 'X'
    
    #Create permutations
    xLen = sep.count('X')
    perms = list(product(range(2),repeat=xLen))

    #Apply permuations
    permArray = []
    for perm in perms:
        newMem = sep.copy()
        perm_index = len(perm)-1
        for i in range(len(newMem)):
            if(newMem[i] == 'X'):
                newMem[i] = str(perm[perm_index])
                perm_index -= 1
        permArray.append(binaryToNumber(''.join(newMem)))

    
    permArray.sort()
    return permArray


def addBinary(bin1):
    sep = list(bin1)
    for b in range(len(bin1)):
        bit = mask[b]
        if(bit.isdigit()):
            sep[b] = bit
    return ''.join(sep)

def numToBinary(number):
    return '{0:036b}'.format(number)

#Here is the controller function for updating memory
def writeToMem(location, number):
    global memValue
    global memLocation

    
    
    #Overwrite memory if location exists
    for mem in addMemMask(location):
        if(memLocation.count(mem) > 0):
            for i in range(memLocation.count(mem)):
                index = memLocation.index(mem)
                del memLocation[index]
                del memValue[index]
        memLocation.append(mem)
        memValue.append(number)

#Gathers Values
for i in range(len(data)):
    if(data[i][:3] == 'mas'):
        #Updates the mask
        mask = data[i].split(' = ')[1]
    
    #Writes number to a new memory location
    if(data[i][:3] == 'mem'):
        #First we need to parse the data
        mem_location_raw, decNum = data[i].split(' = ')
        mem = mem_location_raw[4:-1]

        #Calls funciton to write memory
        writeToMem(int(mem), int(decNum))

#Sum up all the values
total = 0
for num in memValue:
    total += num

print('The sum of all the values are ' + str(total))




