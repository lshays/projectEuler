# prints a list of prime factors of an integer, n
# Assumes n > 1
def getPrimeFactors(n):
    factors = []
    prime = 2
    while n > 1:
        while n % prime == 0:
            factors.append(prime)
            n /= prime
        prime += 1
    return factors

if __name__ == "__main__":
    print getPrimeFactors(600851475143)
