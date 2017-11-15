# What are the first ten digits of the sum of the
# 100 50-digit numbers contained in p013.txt?

# Python automatically converts to the "bignum" type
# when overflow occurs, so this problem is trivial


def generateNumbers(file):
    with open(file, "r") as nums:
        for num in nums:
            yield int(num)


if __name__ == "__main__":
    gen = generateNumbers("p013.txt")
    sum = 0
    for num in gen:
        sum += num
    print str(sum)[0:10]
