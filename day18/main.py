fileName = 'day18/data.txt'
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


def weirdEval(phrase):
    temp = []
    for item in phrase:
        temp.append(item)
        if(len(temp) == 3):

            temp = [str(eval(''.join(temp)))]
    return temp[0]

def calcLine(line):
    #Find Pars tht dont have inner ones
    finished = False
    while not finished:
        mainFinal = []
        tempScan = []
        start = False
        addEnable = True
        par = False
        for item in range(len(line)):
            symbol = line[item]
            mainFinal.append(symbol)
            if(symbol == '('):
                par = True
                begin = len(mainFinal)-1
                linebegin = item
                start = True
            if(symbol == ')' and start):
                start = False
                end = len(mainFinal)-1
                lineend = item
                del mainFinal[begin:end+1]
                mainFinal.append(weirdEval(line[linebegin+1:lineend]))
        if(len(mainFinal) == 1):
            finished = True
        if(not par):
            return weirdEval(mainFinal)
        line = mainFinal.copy()

            
total = 0
for i in data:
    total += int(calcLine(i))

print('The total is : ' + str(total))
        