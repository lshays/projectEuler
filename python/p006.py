def sumOfSquare(l):
    sum = 0
    for num in l:
        sum += num**2
    return sum


def squareOfSum(l):
    sum = 0
    for num in l:
        sum += num
    return sum**2


if __name__ == "__main__":
    print abs(sumOfSquare(range(1, 101)) - squareOfSum(range(1, 101)))
