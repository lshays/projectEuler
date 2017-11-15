# Disclaimer: I have seen this problem before and therefore knew
# the efficient algorithm to solve it


def readFile(filename):
    triangle = []
    with open(filename, 'r') as file:
        for line in file:
            row = []
            for number in line.split():
                row.append(int(number))
            triangle.append(row)
    return triangle


if __name__ == "__main__":
    triangle = readFile("p018.txt")
    length = len(triangle)
    while length > 1:
        for i in range(len(triangle[length-2])):
            triangle[length-2][i] += max(triangle[length-1][i],
                                         triangle[length-1][i+1])
        triangle.pop()
        length -= 1
    print triangle[0][0]
