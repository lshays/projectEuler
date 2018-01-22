n = 3
d = 2

expansion = 1
answer = 0

while expansion <= 1000:
    if len(str(n)) > len(str(d)):
        answer += 1
    newN = n + (2*d)
    newD = n + d
    n = newN
    d = newD
    expansion += 1

print answer
