# Find the sum of all amicable numbers under 10000


def sumOfFactors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum


if __name__ == "__main__":
    answer = 0
    for i in range(2, 10000):
        sum = sumOfFactors(i)
        if sum != i:
            if sumOfFactors(sum) == i:
                answer += i
    print answer
