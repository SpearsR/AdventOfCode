dataFile = open("day6/data.txt", "r")
data = []
for x in dataFile:
    data.append(x.split())
dataFile.close()


def sortAlpha(str):
    temppy = [char for char in str]
    temppy.sort()
    return ''.join(temppy)


def countLettersNotDup(curArr):
    testString = curArr[0]
    tempCount = 0
    ansCount = 0
    validLen = len(curArr)
    for letter in testString: #a,b,d
        for word in curArr: #abd,abgk,abcy
            tempCount += word.count(letter)
        if(tempCount == validLen):
            ansCount += 1
        tempCount = 0
    
    return ansCount

joinedArr = []
temp = []
for item in data:
    if not item:
        joinedArr.append(temp)
        temp = []
    else:
        temp.append(sortAlpha(item[0]))
joinedArr.append(temp)




total = 0
for aStr in joinedArr:
    total += countLettersNotDup(aStr)
    print(aStr)
    print(countLettersNotDup(aStr))

print(total)


