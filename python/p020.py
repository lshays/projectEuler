# find the sum of the digits in the number 100!


# Python's handling of big numbers should make this trivial


def factorial(n):
    ret = 1
    for i in range(2, n+1):
        ret *= i
    return ret


if __name__ == "__main__":
    stringNum = str(factorial(100))
    answer = 0
    for digit in stringNum:
        answer += int(digit)
    print answer
