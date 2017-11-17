# Find the unit fraction (1/n) that has the longest repeating sequence
# n < 1000
# It is given that 1/7 has a repeating sequence of 6 digits

from decimal import Decimal, getcontext, ROUND_FLOOR
# Python decimal module defaults to 28 decimal places


def subSequenceFinder(n):
    for i in range(1, len(n)+1):
        if len(n) % i == 0:
            if n.replace(n[0:i], "") == "":
                return i


# Assumes n is a string
# Returns length of longest sequence found or 0 if none found
def sequenceFinder(n):
    left = n[0:len(n)/2]
    right = n[len(n)/2:]
    while len(right) > 0:
        if left.endswith(right):
            return subSequenceFinder(right)
        else:
            left += right[0]
            right = right[1:]
    return 0


answer = 7
longest = 6
# Couldn't get correct answer without increasing precision considerably
# I'm sure a better solution exists
precision = 10000

for i in range(1, 1000):
    getcontext().rounding = ROUND_FLOOR
    getcontext().prec = precision
    d = str(1/Decimal(i))[2:2+precision]
    while len(d) < precision:
        d += "0"
    temp = sequenceFinder(d)
    if temp > longest:
        longest = temp
        answer = i
print "1 /", answer, "contains a repeating sequence of length:", sequenceFinder(str(1/Decimal(answer))[2:2+precision])
