def oddCompGen():
    c = 2
    d = {}
    while True:
        if c not in d:
            # c is prime
            d[c**2] = [c]
        else:
            # c is composite
            for factor in d[c]:
                d.setdefault(factor+c, []).append(factor)
            del d[c]
            if c % 2 == 1:
                yield c
        c += 1


def twiceASquare():
    n = 1
    while True:
        yield 2*n**2
        n += 1


def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True


gen = oddCompGen()
for oddC in gen:
    squareGen = twiceASquare()
    checker = False
    for square in squareGen:
        if square > oddC:
            break
        if isPrime(oddC - square):
            checker = True
    if checker == False:
        print oddC
        break
