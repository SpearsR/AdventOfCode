fileName = 'day18/testdata.txt'
dataFile = open(fileName, 'r')
data = []
for x in dataFile:
    temp = list(x)
    tempFix = []
    for item in temp:
        if(item != ' '):
            tempFix.append(item)
    data.append(tempFix[:-1])
dataFile.close()

data = data[0]

print(data)

for i in data:
    print(i)
