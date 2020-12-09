dataFile = open("day7/data.txt", "r")
data = []
for x in dataFile:
    temp = []
    temp.append(x[:-2].split(' contain ')[0])
    temp.append(x[:-2].split(' contain ')[1].split(', '))
    data.append(temp)
dataFile.close()

#returns the data for the agrumented bag
def findBag(bagTarget):
    for bag in data:
        if(bag[0] == bagTarget):
            return bag

#returns array of contain bags unless none obv
def findContainBags(bag):
    temp = []
    for conBag in bag:
        if(conBag == 'no other bags'):
            return []
        temp.append(sAtEnd(conBag[2:]))
    return temp

#returns string with a pural s for syntax sake
def sAtEnd(text):
    if(text[-1] != 's'):
        text = text + 's'
    return text

#daddy function
def sift(bag, num):
    bag = bag[0]
    bagData = findBag(bag)
    containData = findContainBags(bagData[1])

    #Break if bag cycle ends
    if not containData:
        doesNotContian.append(bagData[0])
        return 0
    
    #Break if find golden bag
    else:
        if(bag == 'shiny gold bags'):
            doesContain.append(bag)
        else:
            for contBag in containData:
                if(contBag == 'shiny gold bags'):
                    doesContain.append(bag)
                    return 1
    
    #Iterate Bag Count
    for item in containData:
        if(doesContain.count(item) > 0 or item == 'shiny gold bags' ):
            return 1
        elif(doesNotContian.count(item) == 0):
            shinyCount = sift([item], num) 
            if(shinyCount != 0):
                doesContain.append(item)
                return shinyCount
    if(doesNotContian.count(bag) == 0):
        doesNotContian.append(bag)     
    return 0

        
        

#Sift through all the bag and count the shinys ;)
doesNotContian = []
doesContain = []
count = 0
for bag in data:
    count += sift(bag, 0)
    print('Count: '+ str(count) + ' ' +bag[0])

notDup = [] 
doesContain.sort()
for item in doesContain:
    if(doesContain.count(item) > 1):
        print('yup duppy ' + item)
        

print('\n')
doesNotContian.sort()
for item in doesNotContian:
    if(doesNotContian.count(item) > 1):
        print('yup duppy ' + item)

print(len(doesNotContian))
print(len(doesContain))
print(len(data))

print(doesNotContian)
print(doesContain)






