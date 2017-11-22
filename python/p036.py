# Sum of all #'s less than one million that are palindromic
# in both base 10 and base 2


# Assumes n is an integer
# Returns a string
def convertToBinary(n):
    binString = ""
    while n != 0:
        binString = str(n % 2) + binString
        n /= 2
    return binString


# Assumes n is a string
def isPalindrome(n):
    return n == n[::-1]


sum = 0
for i in range(1, 1000000):
    if isPalindrome(str(i)) and isPalindrome(convertToBinary(i)):
        sum += i
print sum
