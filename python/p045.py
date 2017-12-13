def triGen():
    t = 1
    while True:
        yield t*(t+1)/2
        t += 1


def isPent(n):
    return (24*n+1)**0.5 % 6 == 5


def isHex(n):
    return (8*n+1)**0.5 % 4 == 3


for tri in triGen():
    if isPent(tri):
        if isHex(tri):
            print tri
            if tri > 40755:
                break
