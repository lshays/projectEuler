myNum = 2**1000
mySum = 0
myStringNum = str(myNum)
for letter in myStringNum:
    mySum += int(letter)
print mySum
