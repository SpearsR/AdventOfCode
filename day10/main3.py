dataFile = open('day10/testdata.txt', 'r')
data = []
for x in dataFile:
    data.append(int(x))

data.sort()
print(data)

oneDiff = 0
for num in data:
    if(data.count(num+1) == 1):
        oneDiff += 1
twoDiff = 0
for num in data:
    if(data.count(num+2) == 1):
        twoDiff += 1
threeDiff = 0
for num in data:
    if(data.count(num+3) == 1):
        threeDiff += 1

print("oneDiff: " + str(oneDiff) + " twoDiff: " + str(twoDiff) + " threeDiff: " + str(threeDiff))


    

    


total = 1
for item in chunkedData:
    goDeeper(item,item[0],item[-1])
    total*=count
    count = 0

print(total)
    
    






