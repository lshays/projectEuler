def penGen():
    n = 1
    while True:
        yield n*(3*n-1)/2
        n += 1


def isPent(n):
    return (24*n+1)**0.5 % 6 == 5


gen = penGen()
pList = [next(gen), next(gen), next(gen)]
n = 1


while True:
    possibleAnswer = pList[n] + pList[0]
    gap = pList[n] - pList[n-1]
    if pList[0] < gap:
        pList = pList[1:]
        n = 0
    elif isPent(possibleAnswer):
        if isPent(pList[n] - pList[0]):
            print "Answer =", pList[n]-pList[0]
            break
    n += 1
    if n + 1 == len(pList):
        pList.append(next(gen))
