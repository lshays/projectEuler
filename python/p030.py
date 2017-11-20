# Find the sum of all the numbers that can be written
# as the sum of fifth powers of their digits.

# My notes:
# Once a number reaches 7 digits the max value (9^5 * 7)
# does not grow fast enough to have to correct amount of digits.


def sumDigitPowers(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)**5
    return sum


nums = []
for i in range(2, 1000000):
    if sumDigitPowers(i) == i:
        nums.append(i)

print nums
print "sum =", sum(nums)
