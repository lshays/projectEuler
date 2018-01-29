def primeGen():
    d = {}
    n = 2
    while True:
        if n not in d:
            yield n
            d[n**2] = [n]
        else:
            for f in d[n]:
                d.setdefault(n+f, []).append(f)
            del d[n]
        n += 1


def concatNums(a, b):
    return int(str(a) + str(b))


def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def getPrimeList(limit):
    gen = primeGen()
    prime = next(gen)
    pl = []
    while prime <= limit:
        pl.append(prime)
        prime = next(gen)
    return pl

pl = getPrimeList(1000)
import itertools
primeSets = list(itertools.permutations(pl, 5))

length = len(pSet)
count = 0
for pSet in primeSets:
    count += 1
    found = True
    for a in pSet:
        for b in pSet:
            if a == b:
                continue
            num = concatNums(a, b)
            if not isPrime(num):
                found = False
    print count, "/", length
    if found:
        print pSet
        break
