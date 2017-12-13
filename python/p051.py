import sys

def primeGen():
    p = 2
    d = {}
    while True:
        if p not in d:
            d[p**2] = [p]
            yield p
        else:
            for f in d[p]:
                d.setdefault(f+p, []).append(f)
            del d[p]
        p += 1


def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def starString(s, n):
    return n*'x' + (len(s)-n)*'*'


def permGen(s):
    if len(s) <= 1:
        yield s
    else:
        for perm in permGen(s[1:]):
            for i in range(len(s)):
                yield perm[:i] + s[0:1] + perm[i:]


gen = primeGen()
primeSet = set()
primeSet.add(next(gen))
while max(primeSet) < 100000:
    primeSet.add(next(gen))


nonPrimes = 0
reset = False
gen = primeGen()
l = 1000
while True: 
    prime = str(next(gen))
    if l < len(prime):
        reset = True
    else:
        reset = False
    l = len(prime)
    print prime
    if reset:
        primeSet = set([x for x in  primeSet if len(str(x)) == len(str(prime))])
    for i in range(1, len(prime)):
        for perm in permGen(starString(prime, i)):
            if perm[-1] == "x":
                continue
            for x in map(str, range(0, 10)):
                myString = perm.replace("x", x) 
                for c in range(len(myString)):
                    if myString[c] == "*":
                        myString = myString.replace("*", prime[c], 1)
                if int(myString) not in primeSet or myString[0] == "0": 
                    nonPrimes += 1
                if nonPrimes > 3:
                    break
            if nonPrimes <= 3:
                print "Answer =", prime
                sys.exit()
            nonPrimes = 0
