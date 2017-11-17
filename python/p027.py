# n^2 + an + b
# |a| < 1000
# |b| <= 1000

# Find the pair of numbers, a and b that produce
# the most consecutive primes using the above formula

# It is known that 1 and 41 produce 40 consecutive primes

aa = 1
bb = 41
con = 40


def primeSieve():
    p = 2
    d = {}
    while True:
        if p not in d:
            yield p
            d[p**2] = [p]
        else:
            for x in d[p]:
                d.setdefault(p+x, []).append(x)
                del d[p]
        p += 1


gen = primeSieve()
primeList = [next(gen)]
for a in range(-999, 1000):
    for b in range(-999, 1000, 2):
        n = 0
        product = n**2 + a*n + b
        while product > primeList[len(primeList)-1]:
            primeList.append(next(gen))
        while product in primeList:
            n += 1
            product = n**2 + a*n + b
        if n+1 > con:
            con = n+1
            aa = a
            bb = b
print aa, bb, aa*bb
