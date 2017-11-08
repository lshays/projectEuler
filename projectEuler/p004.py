# Determines if a number is a palindrome
# Assumes n is an Integer
def isPalindrome(n):
    return str(n) == str(n)[::-1]

#Finds the largest palindrome made from the product of two three-digit numbers
def threeDigitPalindrome():
    largest = 0
    for i in range(1000,99,-1):
        for j in range(1000,99,-1):
            if i*j > largest and isPalindrome(i*j):
                largest = i*j
    return largest

if __name__ == "__main__":
    print threeDigitPalindrome()
