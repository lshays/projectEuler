# Find the sum of all numbers which are equal
# to the sum of the factorial of their digits.


# My Notes:
#
# Number must have at least two digits to be considered a sum
# Number must have less than 8 digits otherwise sum won't be large enough


lookupTable = {
        "0": 1,
        "1": 1,
        "2": 2,
        "3": 6,
        "4": 24,
        "5": 120,
        "6": 720,
        "7": 5040,
        "8": 40320,
        "9": 362880,
}


total = 0
for i in range(10, 10000000):
    sum = 0
    print i
    for digit in str(i):
        sum += lookupTable[digit]
    if sum == i:
        total += i

print "Total:", total
