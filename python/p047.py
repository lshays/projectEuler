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


def getPrimeFactors(n, l):
    if n == 1:
        return []
    for p in l:
        if n % p == 0:
            return [p] + (getPrimeFactors(n/p, l))


i = 2
consec = 0
gen = primeGen()
primes = [next(gen)]
while True:
    while i > primes[-1]:
        primes.append(next(gen))
    f = set(getPrimeFactors(i, primes))
    if len(f) >= 4:
        consec += 1
    else:
        consec = 0
    if consec == 4:
        print i, getPrimeFactors(i, primes)
        print i-1, getPrimeFactors(i-1, primes)
        print i-2, getPrimeFactors(i-2, primes)
        print i-3, getPrimeFactors(i-3, primes)
        break
    i += 1
