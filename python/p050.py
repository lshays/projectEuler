def primeGen():
    p = 2
    d = {}
    while True:
        if p not in d:
            yield p
            d[p**2] = [p]
        else:
            for f in d[p]:
                d.setdefault(f+p, []).append(f)
            del d[p]
        p += 1


def isPrime(n):
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    return True

#limit = 1000000
#primeList = []
#gen = primeGen()
#while True:
#    prime = next(gen)
#    if prime > limit:
#        break
#    else:
#        primeList.append(prime)
#
#i = 0
#answer = 0
#length = 0
#while i < len(primeList):
#    mySum  = 0
#    print i, len(primeList)
#    for n in range(i, len(primeList)):
#        mySum += primeList[n]
#        if mySum < limit and isPrime(mySum):
#            if n-i > length:
#                length = n-i
#                answer = mySum
#    i += 1


limit = 1000000
primeList = []
gen = primeGen()
while True:
    prime = next(gen)
    if prime > limit:
        break
    else:
        primeList.append(prime)

i = 0
answer = 0
length = 0
while i < len(primeList):
    mySum  = 0
    print i, len(primeList)
    for n in range(i, len(primeList)):
        mySum += primeList[n]
        if mySum > limit:
            break
        if n-i < length:
            continue
        if isPrime(mySum):
            length = n-i
            answer = mySum
    i += 1

print answer, length+1 
