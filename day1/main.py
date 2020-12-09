#Gather Data
dataFile = open("day1/data.txt", "r")
data = []
for x in dataFile:
    data.append(int(x))
dataFile.close()

#Finds the two numbers
for num in data:
    for num2 in data:
        for num3 in data:
            if(num + num2 + num3  == 2020):
                print(num)
                print(num2)
                print(num3)

