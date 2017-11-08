singleDigitDict = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
doubleDigitDict = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
        19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}
H = "hundred"
T = "onethousand"
A = "and"

mySum = 0

def getNum(n):
    if n == 0:
        return ""
    elif len(str(n)) == 4:
        return T + str(getNum(int(str(n)[1:])))
    elif len(str(n)) == 3:
        if int(str(n)[1:]) != 0:
            return str(getNum(int(str(n)[0:1]))) + H + A + str(getNum(int(str(n)[1:])))
        else:
            return str(getNum(int(str(n)[0:1]))) + H
    elif len(str(n)) == 2:
        if n < 20:
            return doubleDigitDict[n]
        else:
            return doubleDigitDict[int(str(n)[0:1]+"0")] + str(getNum(int(str(n)[1:])))
    elif len(str(n)) == 1:
        return singleDigitDict[n]
    else:
        return ""

for i in range(1001):
    mySum += len(getNum(i))

for i in range(100):
    print getNum(i)

print mySum
