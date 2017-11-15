# Given the collatz sequence, what number under 1 million
# generates the most terms?


def collatzSequence(n):
    if n % 2 == 0:
        return n/2
    return 3*n+1


if __name__ == "__main__":
    longest = 0
    answer = 0
    D = {}
    for i in range(2, 1000000):
        temp = i
        length = 1
        while temp != 1:
            temp = collatzSequence(temp)
            if temp in D:
                length += D[temp]
                break
            length += 1
        D[i] = length
        if length > longest:
            longest = length
            answer = i
    print answer
