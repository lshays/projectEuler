numberFile = open("p13Numbers.txt", 'r')
myNumbers = []
digits = ""
for line in numberFile:
    myNumbers.append(line.strip('\n'))
for i in range(10):
    tempSum = 0
    for number in myNumbers:
        tempSum += int(number[i])

