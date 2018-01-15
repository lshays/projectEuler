def combo(n, r):
    ret = 1
    for x in range(n, r, -1):
        ret *= x
    for x in range(n-r, 0, -1):
        ret /= x
    return ret


total = 0
for n in range(23, 101):
    for r in range(1, n):
        if combo(n, r) > 1000000:
            total += 1
print total
