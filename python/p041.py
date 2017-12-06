# Initial solution tooks ~2.5 minutes
#
# After reading project Euler forums, I discovered that 
# 8 or 9 digit solutions would not work since they are
# always divisible by 3.
#
# New Solution takes less than a second

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


answer = 0
digits = 7
while answer == 0:
    for perm in all_perms(range(1, digits+1)):
        perm = [str(x) for x in perm]
        perm = int("".join(perm))
        if isPrime(perm):
            if perm > answer:
                answer = perm
    digits -= 1
print answer
