dataFile = open('day9/data.txt', 'r')
data = []
for x in dataFile:
    data.append(int(x))

def validNextNumber(num, preamble):
    valid = False
    for number in preamble:
        if valid == True:
            break
        for number2 in preamble:
            if(number != number2):
                if((number + number2) == num):
                    print(str(number) + " + " + str(number2) + " = " + str(num))
                    valid = True
                    break
    return valid

def sumArray(arr):
    global breakNumber
    total = 0
    for number in arr:
        total += number
        if(total == breakNumber):
            print(arr)
    return total


#Declaring the preamble varible
globalPreamble = data[0:25]
index = 0
for i in range(len(data) - 25):
    if(validNextNumber(data[index+25], globalPreamble)):
        index += 1
        globalPreamble = data[index:index+25]
    else: 
        breakNumber = data[index + 25]
        print(str(breakNumber) + ' is the wrong number in the list. Index: ' + str(index))
        break


#Find all contigeus sets of numbers before index 476
contSet = []
forTesting = []

newData = data[:501]

newSet = True
setFound = False
temp = []
contIterate = -1
onIndex = 0
while not setFound:
    if setFound:
        break
    try:
        contIterate+=1
        total = 0
        for i in range(len(data)):
            total += data[i + onIndex]
            temp.append(data[i + onIndex])
            if(total > breakNumber):
                break
            elif(total == breakNumber):
                print(temp)
                print(temp[0]+ temp[-2])
                print(total)
                print(sumArray(temp))
                print(min(temp)+ max(temp))
                print(min(temp))
                print(max(temp))
                
                setFound = True
        onIndex +=1
        temp = []

    except:
        print('Fuck')
        break
        

    


