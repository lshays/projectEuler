# I observed simple pattern that emerged for this problem.
# No real algorithm required.

sum = 1
index = 1
add = 2
dimensions = 1

while dimensions < 1001:
    sum += 4 * index + 10 * add
    index = index + 4 * add
    dimensions += 2
    add += 2

print sum

