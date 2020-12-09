dataFile = open("day8/data.txt", "r")
data = []
for x in dataFile:
    data.append(x.split())
dataFile.close()

lineIndex = 0

#Accumulation Function, adds or subtracts
def accumulate(arg, num):
    operation = arg[0]
    acc = arg[1:]

    if(operation == '-'):
        num -= int(acc)
    else:
        num += int(acc)
    

    global lineIndex 
    lineIndex += 1
    return num
#Jump, Go ahead and JUMP
def jumpSki(arg,index):
    operation = arg[0]
    acc = arg[1:]

    if(operation == '-'):
        index -= int(acc)
    else:
        index += int(acc)
    
    global lineIndex 
    lineIndex = index

    if(int(acc) == 0):
        lineIndex += 1


#Stores lines run to check double usage
def runStack():
    global linesExecuted
    linesExecuted = []
    global lineIndex
    lineIndex = 0
    global count
    count = 0
    secondTime = False
    atEnd = False
    while(not secondTime and not atEnd):
        try:
            lineCode = data[lineIndex]
        except:
            print('Ripppppppp')
            linesExecuted.append(lineIndex)
            atEnd = True
            return True


        if(linesExecuted.count(lineIndex) <= 1):
            if(lineCode[0] == 'acc'):
                count = accumulate(lineCode[1],count)
                print(':'.join(lineCode) + " ------> " + 'Count: ' + str(count) + ' Index: ' + str(lineIndex))
                linesExecuted.append(lineIndex)
            elif(lineCode[0] == 'jmp'):
                jumpSki(lineCode[1],lineIndex)
                print(':'.join(lineCode) + " ------> " + 'Count: ' + str(count) + ' Index: ' + str(lineIndex))
                linesExecuted.append(lineIndex)
            else:
                lineIndex += 1
                print(':'.join(lineCode) + " ------> " + 'Count: ' + str(count) + ' Index: ' + str(lineIndex))
                linesExecuted.append(lineIndex)
        else:
            print('Line ' + str(lineIndex) + " ran a second time")
            secondTime = True
            return False




iteration= -1
for i in range(len(data)):
    lineIndex = 0
    iteration += 1
    switchBack = data[i]
    targetCode = data[i][0]
    if(targetCode == 'nop'):
        data[i][0] = 'jmp'
        if(runStack()):
            print('yup, here is the fucker ' + str(iteration))
            break
        data[i][0] = 'nop'
    elif(targetCode == 'jmp'):
        data[i][0] = 'nop'
        if(runStack()):
            print('yup, here is the fucker ' + str(iteration))
            break
        data[i][0] = 'jmp'



       
    


print(count)


