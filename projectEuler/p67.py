def readTriangle(triFile, triList):
    for line in triFile:
        tempList = []
        for number in line.strip('\n').split(' '):
            tempList.append(int(number))
        triList.append(tempList)

myTri = []
myTriFile = open("bigTriangle.txt", "r")
readTriangle(myTriFile, myTri)

for i in reversed(range(len(myTri)-1)):
    newRow = []
    count = 0
    for number in myTri[i]:
        newRow.append(max(myTri[i+1][count],myTri[i+1][count+1]) + number)
        count += 1
    myTri.pop()
    myTri[len(myTri)-1] = newRow

print myTri[0][0]
