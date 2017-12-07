def getPerms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in getPerms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


# Assumes l is a list of strings
def hasProp(l):
    if int("".join(l[1:4])) % 2 == 0:
        if int("".join(l[2:5])) % 3 == 0:
            if int("".join(l[3:6])) % 5 == 0:
                if int("".join(l[4:7])) % 7 == 0:
                    if int("".join(l[5:8])) % 11 == 0:
                        if int("".join(l[6:9])) % 13 == 0:
                            if int("".join(l[7:])) % 17 == 0:
                                return True
    return False


permGen = getPerms([str(x) for x in range(10)])
sum = 0
for perm in permGen:
    if hasProp(perm):
        sum += int("".join(perm))
print sum
