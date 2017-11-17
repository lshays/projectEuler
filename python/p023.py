# Sum of positive integers that cannot be expressed as the sum
# of two abundant numbers. Upper limit is 28123


def isAbundant(n):
    sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum += i
            if n/i != i:
                sum += n/i
    return sum > n


if __name__ == "__main__":
    abundants = []
    sums = []
    for i in range(12, 28124):
        if isAbundant(i):
            abundants.append(i)
    for i in abundants:
        for j in abundants:
            if i+j < 28124:
                sums.append(i+j)
    sums = set(sums)
    print sum(range(1, 28124)) - sum(sums)
