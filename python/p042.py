def letterScore(word):
    score = 0
    for letter in word.lower(): #97-122
        ascii = ord(letter)
        if ascii >= 97 and ascii <= 122:
            score += ascii - 96 
    return score


def triGenerator():
    n = 1
    while True:
        yield 0.5*n*(n+1)
        n += 1

gen = triGenerator()
triNums = [next(gen)]
myMax = max(triNums)

answer = 0

with open("p042.txt", 'r') as file:
    for line in file:
        for word in line.split(','):
            score = letterScore(word)
            while score > myMax:
                triNums.append(next(gen))
                myMax = max(triNums) 
            if score in triNums:
                answer += 1

print answer

