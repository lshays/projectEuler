# Find the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.


# My Notes: You should only have to go up to 9,999
# because all numbers 10000+ are going to have at
# least 10 digits in their mmp combo


def listFactors(n):
    factors = [[1, n]]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append([i, n/i])
    return factors


sum = 0
panDigits = set([str(i) for i in range(1, 10)])

for i in range(1000, 10000):
    factors = listFactors(i)
    product = str(i)
    for factorPair in factors:
        multiplicand = str(factorPair[0])
        multiplier = str(factorPair[1])
        if len(multiplier) + len(multiplicand) + len(product) == 9:
            myDigits = set()
            for digit in multiplier + multiplicand + product:
                myDigits.add(digit)
            if myDigits.issuperset(panDigits):
                print i, multiplier, multiplicand
                sum += i
                break
print sum
