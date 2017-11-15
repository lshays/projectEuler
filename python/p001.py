# Sums all numbers < n that are multiples of m*
# Assumes n > 0 and *m contains at least one argument
def sumMultiples(n, *m):
    sum = 0
    for i in range(1,n):
        for num in m:
            if i % num == 0:
                sum += i
                break
    return sum

if __name__ == "__main__":
    print sumMultiples(1000, 3, 5)
