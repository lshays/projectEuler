def isPalindrome(n):
    return str(n) == str(n)[::-1]

def reverseAdd(n):
    return n + int(str(n)[::-1])

num = 1
answer = 0
while num < 10000:
    numToTest = num
    for i in range(50):
        numToTest = reverseAdd(numToTest)
        if isPalindrome(numToTest):
            break
        if i == 49:
            print num, numToTest
            answer += 1
    num += 1

print answer

