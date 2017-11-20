# n^2 + an + b
# |a| < 1000
# |b| <= 1000

# Find the pair of numbers, a and b that produce
# the most consecutive primes using the above formula

# It is known that 1 and 41 produce 40 consecutive primes


def isPrime(n):
    if n < 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


aS = range(-999, 1000)
bS = range(1, 1000, 2)
mySet = set()

for a in aS:
    for b in bS:
        mySet.add((a, b))

n = 0
while len(mySet) > 1:
    tempSet = set()
    for a, b in mySet:
        num = n**2 + a*n + b
        if not isPrime(num):
            tempSet.add((a, b))
    mySet = mySet - tempSet
    n += 1

answer = mySet.pop()
print answer, "=", answer[0] * answer[1]
print n, "consecutive primes"
