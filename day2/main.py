dataFile = open("day2/data.txt", "r")
data = []
valid = []
for x in dataFile:
    data.append(x.split())
dataFile.close()

for item in data:
    
    #Call Varibles
    lower = int(item[0].split('-')[0]) -1
    higher = int(item[0].split('-')[1]) - 1
    count = 0
    testLetter = str(item[1].split(':')[0])
    letters = list(item[2])


    #Counts the letters based on the test letter
    if(letters[lower] == testLetter):
        count += 1
    
    if(letters[higher] == testLetter):
        count += 1
    

    
    #Checks bounds
    if(count == 1):
        valid.append(item)

        



print(len(valid))
