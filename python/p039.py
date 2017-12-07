d = {}
for p in range(10, 1001, 2):
    d[p] = 0
    print p
    for c in range(p/3+1, p):
        for a in range(1, c):
            b = (c**2 - a**2)**0.5
            if a+b+c == p:
                d[p] += 1


answer = (0,0)
for key in d:
    if d[key] > answer[1]:
        answer = (key, d[key])
print "..."
print answer
