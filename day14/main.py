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

    #First let's convert our number to a binary string
    newBinary = numToBinary(number)
    #Now lets add the binary number to the mask
    masked = addBinary(newBinary)
    #Coverted to a decimal number
    newValue = binaryToNumber(masked)
    
    #Overwrite memory if location exists
    if(memLocation.count(location) > 0):
        index = memLocation.index(location)
        del memLocation[index]
        del memValue[index]
        memLocation.insert(index, location)
        memValue.insert(index, newValue)
    else:
        memLocation.append(location)
        memValue.append(newValue)

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




