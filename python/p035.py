# How many circular primes are there below one million?


def primeSieve():
    num = 2
    composites = {}
    
    while(True):
        if num not in composites:
            # num is primes
            composites[num**2] = [num]
            yield num
        else:
            for factor in composites[num]:
                composites.setdefault(num + factor, []).append(factor)
        num += 1


gen = primeSieve()
primes = set()
prime = next(gen)
while prime < 1000000:
    primes.add(prime)
    prime = next(gen)

total = 0

for prime in primes:
    myNum = str(prime)
    circular = True
    for i in range(len(myNum)-1):
        start = myNum[0]
        myNum = myNum[1:] + start
        if int(myNum) not in primes:
            circular = False
    if circular:
        total += 1


print "total:", total
