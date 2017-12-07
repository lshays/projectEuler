def concatNums(a, b):
    return int(str(a) + str(b))


def isPandigital(n):
    if len(str(n)) != 9:
        return False
    mySet = set()
    for digit in str(n):
        mySet.add(digit)
    mySet.discard("0")
    return len(mySet) == 9



answer = 0
for i in range(1,10000):
    myNum = i
    n = 2
    while len(str(myNum)) < 9:
        myNum = concatNums(myNum, n*myNum)
        n += 1
    if isPandigital(myNum):
        answer = max(myNum, answer)

print answer
