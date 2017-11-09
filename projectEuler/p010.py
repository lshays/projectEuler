# Find the sum of all primes below 2 million


# Prime number generator based on Sieve of Eratosthenes
def sieveOfEratosthenes():
    composites = {}
    testNum = 2
    while True:
        if testNum not in composites:
            # testNum is prime
            yield testNum
            composites[testNum**2] = [testNum]
        else:
            # testNum is composite
            for factor in composites[testNum]:
                composites.setdefault(testNum + factor, []).append(factor)
            del composites[testNum]
        testNum += 1


if __name__ == "__main__":
    totalSum = 0
    prime = 0
    generator = sieveOfEratosthenes()
    while prime < 2000000:
        totalSum += prime
        prime = next(generator)
    print totalSum
