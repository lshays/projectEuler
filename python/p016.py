# What is the sum of the digits of the number 2^1000?

# Once again python's handling of large numbers makes this
# problem trivial
if __name__ == "__main__":
    num = 2**1000
    sum = 0
    for digit in str(num):
        sum += int(digit)
    print sum
