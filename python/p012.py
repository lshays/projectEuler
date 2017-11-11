# What is the value of the first triangle number to have over 500 divisors?

def getDivisors(n):
    divisors = 2
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            divisors += 2
    return divisors


def triGenerator():
    tri = 1
    add = 2
    while True:
        yield tri
        tri += add
        add += 1


if __name__ == "__main__":
    divs = 0
    gen = triGenerator()
    done = False
    while not done:
        tri = next(gen)
        divs = getDivisors(tri)
        if divs > 500:
            print tri
            done = True
