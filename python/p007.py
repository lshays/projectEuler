# What is the 10,001st prime number?

# Based on sieve of erastothenes, from post on stackoverflow
def primeNumberGenerator():
    myNum = 2
    composites = {}
    while True:
        if myNum not in composites:
            # myNum is prime
            composites[myNum**2] = [myNum]
            yield myNum
        else:
            # myNum is composite
            for num in composites[myNum]:
                composites.setdefault(myNum+num, []).append(num)
            del composites[myNum]
        myNum += 1


if __name__ == "__main__":
    gen = primeNumberGenerator()
    for i in range(10000):
        next(gen)
    print next(gen)
