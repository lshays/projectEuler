# What is the value of the first triangle number to have over 500 divisors?

def getDivisors(n):
    divisors = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisors += 1
    return divisors


