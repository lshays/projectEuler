def isPrime(n):
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    return True


for i in range(1001, 10000-6660, 2):
    if isPrime(i):
        if isPrime(i+3330):
            if isPrime(i+6660):
                set1 = set()
                set2 = set()
                for digit in str(i):
                    set1.add(digit)
                    set2.add(digit)
                for digit in str(i+3330):
                    set2.add(digit)
                for digit in str(i+6660):
                    set2.add(digit)
                if len(set1) == len(set2):
                    print i, i+3330, i+6660
