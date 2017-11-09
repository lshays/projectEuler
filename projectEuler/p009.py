# Given two facts:
# a^2 + b^2 == c^2
# a + b + c = 1000
# Find the product abc


import sys

# Using some handwritten algebra, I simplified the above
# two equations to this
def simplifiedEquation(a, b):
    return 500000 - 1000*a - 1000*b + (a*b) == 0

# To solve, test all numbers 1-1000 for a and b
# Once a and b are found, solve for c
if __name__ == "__main__":
    for a in range(1, 1000):
        for b in range(1, 1000-a):
            if simplifiedEquation(a, b):
                c = int((a**2 + b**2)**0.5)
                print "a =", a
                print "b =", b
                print "c =", c
                print "a*b*c = ", a*b*c
                sys.exit(0)
