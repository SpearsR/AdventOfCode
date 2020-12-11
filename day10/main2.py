dataFile = open('day10/data.txt', 'r')
data = []
for x in dataFile:
    data.append(int(x))

data.sort()
count = 0
deviceJolts = max(data) + 3
tempPerms = []

#this will return the next array 'chunk'
def whatsNext(arr):
    count = 0
    index = 0
    went = 0
    atOnly = False
    justOne = False
    while not atOnly: 
        backcount = 0
        can3, can2, can1 = False, False, False
        num = arr[index]
        if(arr.count(num + 1) == 1):
            count += 1
            can1 = True
            if(arr.count(num-1) == 1):
                backcount += 1
            if(arr.count(num-2) == 1):
                backcount += 1
            
        if(arr.count(num + 2) == 1):
            count += 1
            can2 = True
            if(arr.count(num+1) == 1):
                backcount += 1
            if(arr.count(num) == 1):
                backcount += 1

        if(arr.count(num + 3) == 1):
            count += 1
            can3 = True
            if(arr.count(num+1) == 1):
                backcount += 1
            if(arr.count(num+2) == 1):
                backcount += 1
        
    
        
        if( backcount == 0 and (count == 1 or count == 0)):
            atOnly =True
            onlyNum = num
            if(went == 0):
                justOne = True
            break

        if(can3):
            index = arr.index(num+3)
        elif(can2):
            index = arr.index(num+2)
        elif(can1):
            index = arr.index(num+1)

        count = 0
        went += 1
    if(justOne):
        return [arr[0]]
    else:
        return arr[:arr.index(onlyNum)+1]

#now we need to seperate all these chunks
newData = data.copy()
chunkedData = []
def getChunks():
    notFinished = True
    index = 0
    chunkedData.append(whatsNext(newData))
    while notFinished:
        try:
            nextNum = newData.index(chunkedData[index][-1]) + 1
            chunkedData.append(whatsNext(newData[nextNum:]))
            index += 1

        except:
            notFinished = False


def goDeeper(arr,jolt,last,passOver):
    global count
    #This counts all possible jumps
    if(arr.count(jolt + 1) == 1):
        arr1 = passOver.copy()
        arr1.append(jolt+1)
        goDeeper(arr,jolt+1, last, arr1)
    if(arr.count(jolt + 2) == 1):
        arr2 = passOver.copy()
        arr2.append(jolt+2)
        goDeeper(arr,jolt+2, last,arr2)
    if(arr.count(jolt + 3) == 1 or (jolt + 3) == deviceJolts):
        arr3 = passOver.copy()
        arr3.append(jolt+3)
        goDeeper(arr,jolt+3, last,arr3)

    if(jolt == last):
        count += 1
        print(passOver)


getChunks()
#Adding only permuable items to a 
print(chunkedData)
print(count)




total = 1
for item in chunkedData:
    goDeeper(item,item[0],item[-1],[item[0]])
    total*=count
    count = 0

print(total)
print(chunkedData)
    





