def digitSum(n):
    mySum = 0
    for digit in str(n):
        mySum += int(digit)
    return mySum

answer = 0
for a in range(1, 100):
    for b in range(1, 100):
        x = digitSum(a**b)
        if x > answer:
            answer = x

print answer

