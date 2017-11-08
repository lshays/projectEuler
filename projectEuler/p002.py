# Sums even fibonnaci numbers <= n
# Assumes n >= 1
def sumEvenFibs(n):
    sum = 0
    oldfib = 1
    fib = 1
    while fib <= n:
        if fib % 2 == 0: sum += fib
        newFib = fib + oldfib
        oldfib = fib
        fib = newFib
    return sum

if __name__ == "__main__":
    print sumEvenFibs(4000000)
