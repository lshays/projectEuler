import sys

# Initially I got an answer of 120383. This prime turns into *2*3*3,
# which leads to the correct answer of 121313. However, I would suggest
# a rewording of the problem. Technically, 120383 is the lowest prime 
# that can have certain digits replaced with the same number yielding
# a family of 8+ primes.
#
# *** It is not part of the family itself though ***
#
# This confused me initially and if I had known that going in I think
# I would have been able to find a more elegant, efficient solution.

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
while next(gen) < 97:
    pass
while True:
    prime = str(next(gen))
    print "Testing:", prime
    for i in range(len(prime)-1):
        starStr = starString(prime[0:-1], i)
        permSet = set()
        for perm in permGen(starStr):
            permSet.add(perm)
        for perm in permSet:
            myString = ""
            for c in range(len(perm)):
                if perm[c] == "*":
                    myString += "*"
                else:
                    myString += prime[c]
            myString += prime[-1]
            nonPrimes = 0
            pl = []
            for i in range(10):
                primeString = myString.replace("*", str(i))
                if primeString[0] == "0":
                    nonPrimes += 1
                    continue
                if not isPrime(int(primeString)):
                    nonPrimes += 1
                    if nonPrimes > 2:
                        break
                else:
                    pl.append(primeString)
            if nonPrimes <= 2:
                print "ANSWER =", pl[0] 
                print "(" + myString + ")", "--->", pl
                sys.exit()
