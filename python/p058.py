def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


sideLength = 3
ratio = 1.0
num = 1
primes = 0

while ratio > 0.10:
    for i in range(4):
        num += (sideLength-1)
        if isPrime(num):
            primes += 1
    ratio = float(primes) / ((2*sideLength)-1) 
    print sideLength, ratio
    sideLength += 2
