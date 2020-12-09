dataFile = open("day7/data.txt", "r")
data = []
for x in dataFile:
    temp = []
    temp.append(x[:-2].split(' contain ')[0])
    temp.append(x[:-2].split(' contain ')[1].split(', '))
    data.append(temp)
dataFile.close()

print(data)
#returns the data for the agrumented bag
def findBag(bagTarget):
    for bag in data:
        if(bag[0] == bagTarget):
            return bag

#returns array of contain bags unless none obv
def findContainBags(bag):
    temp = []
    subtemp =[]
    for conBag in bag:
        if(conBag == 'no other bags'):
            return []
        subtemp.append(int(conBag[:1]))
        subtemp.append(sAtEnd(conBag[2:]))
        temp.append(subtemp)
        subtemp = []
    return temp

#returns string with a pural s for syntax sake
def sAtEnd(text):
    if(text[-1] != 's'):
        text = text + 's'
    return text

#main function
def sift(bag, num):
    bag = bag[0]
    bagData = findBag(bag)
    containData = findContainBags(bagData[1])

    #Break if bag cycle ends
    if not containData:
        bagNumber.append(bagData[0])
        numNumber.append(0)
        return 0
    
    #Counts bags directly
    else:
        for contBag in containData:
            siftedNum = sift([contBag[1]], 0)
            num += contBag[0] + (contBag[0] * siftedNum)
    
        bagNumber.append(bag)
        numNumber.append(siftedNum)          
        return num

        
        

#Sift through all the bag and count the shinys ;)
bagNumber = []
numNumber = []

count = sift(['shiny gold bags'],0)
print(count)






