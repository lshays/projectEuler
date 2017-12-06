numString = ""
i = 1
while len(numString) < 1000000:
    numString += str(i)
    i += 1

answer = 1
multiplicand = 1
while multiplicand <= 1000000:
    answer *= int(numString[multiplicand-1])
    multiplicand *= 10

print "yeet"
