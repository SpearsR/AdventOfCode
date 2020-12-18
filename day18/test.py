import re
string = '1+2*3+4*5+6'
arr = list(string)

def evalCalc(arr):
    mults = []
    for item in arr:
        if(item == '*'):
            mults.append('*')
        if(item == '/'):
            mults.append('/')
    temp = re.split('[*/]', ''.join(arr))
    print(temp)
    tempNew = []
    for i in temp:
        tempNew.append(str(eval(i)))


    for i in range(len(mults)):
        tempNew.insert(i*2+1,mults[i])
    
    tempNew = ''.join(tempNew)
    return str(eval(tempNew))


print(evalCalc(arr))

