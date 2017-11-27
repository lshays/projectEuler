def primeSieve():
    comps = {}
    num = 2
    while True:
        if num not in comps:
            comps[num**2] = [num]
            yield num
        else:
            for factor in comps[num]:
                comps.setdefault(factor + num, []).append(factor)
            del comps[num]
        num += 1


def truncatable(n, primeList):
    prime = str(n)
    if len(prime) <= 1:
        return False
    for i in range(1, len(prime)):
        if int(prime[i:]) not in primeList:
            return False
        if int(prime[:len(prime)-i]) not in primeList:
            return False
    return True
        

truncPrimes = []
primes = set()
gen = primeSieve()

while len(truncPrimes) < 11:
    prime = next(gen)
    primes.add(prime)
    if truncatable(prime, primes):
        truncPrimes.append(prime)

print truncPrimes
print sum(truncPrimes)
