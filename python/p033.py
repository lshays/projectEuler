prod = 1
for n in range(10, 100):
    for d in range(10, 100):
        if n >= d:
            continue
        if str(n)[1] != str(d)[0]:
            continue
        try:
            if int(str(n)[0]) / float(str(d)[1]) == n / float(d):
                print n, "/", d
                prod *= (n / float(d))
        except ZeroDivisionError:
            pass

print prod
