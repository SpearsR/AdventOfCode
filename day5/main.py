dataFile = open("day5/data.txt", "r")
data = []
for x in dataFile:
    data.append(x.split()[0])
dataFile.close()


seatIds = []
for codePass in data:
    row = [0, 127] #[0,127] FBFBBFF
    col = [0, 7]
    tempArr = list(codePass)
    for i in range(7):
        diffHalf = int((row[1] - row[0])/2)
        newRowArr = [[row[0], row[1] - diffHalf - 1], [row[0] + (diffHalf + 1), row[1]]]
        if(tempArr[i] == 'F'):
            row = newRowArr[0]
        elif(tempArr[i] == 'B'):
            row = newRowArr[1]
    for c in range(3):
        diffHalf = int((col[1] - col[0])/2)
        newRowArr = [[col[0], col[1] - diffHalf - 1], [col[0] + (diffHalf + 1), col[1]]]
        if(tempArr[c+7] == 'L'):
            col = newRowArr[0]
        elif(tempArr[c+7] == 'R'):
            col = newRowArr[1]
    seatIds.append((row[0] * 8) + col[0])

print(max(seatIds))

seatIds.sort()

count = 11
for seat in seatIds:
    count += 1
    if(seat != count):
        print(count)
        break


