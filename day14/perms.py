from itertools import permutations

mask = '000000000000000000000000000000X1001X'

def binaryToNumber(bin):
    return int(bin,2)

def numToBinary(number):
    return '{0:036b}'.format(number)


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
    os = ''
    for i in range(xLen):
        os += '0'
    ones = ''
    for i in range(xLen):
        ones += '1'
    onesand0 = os + ones
    perms = permutations(onesand0, xLen)
    print(perms)
    perms = list(dict.fromkeys(perms))
    print(perms)




    #Apply permuations
    permArray = []
    for perm in perms:
        newMem = sep.copy()
        perm_index = len(perm)-1
        for i in range(len(newMem)):
            if(newMem[i] == 'X'):
                newMem[i] = perm[perm_index]
                perm_index -= 1
        permArray.append(binaryToNumber(''.join(newMem)))

    
    permArray.sort()
    return permArray
    



print(addMemMask(42))