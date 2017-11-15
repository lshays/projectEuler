# Given graph from p011grid.txt, find max product
# of 4 adjacent numbers in same direction


# Read grid row by row into graph
def readGrid(file):
    graph = []
    with open(file, 'r') as grid:
        for line in grid.readlines():
            row = []
            for number in line.strip().split(" "):
                row.append(int(number))
            graph.append(row)
    return graph


# gets next adjacent node of graph[r][c] in direction d
# returns 1 if edge node
def getNextAdjacent(graph, r, c, d):
    if d == "right":
        try:  # right
            return graph[r][c+1]
        except IndexError:
            return 1
    elif d == "left":
        try:  # left
            return graph[r][c-1]
        except IndexError:
            return 1
    elif d == "upper right":
        try:  # upper right
            return graph[r+1][c+1]
        except IndexError:
            return 1
    elif d == "lower right":
        try:  # lower right
            return graph[r-1][c+1]
        except IndexError:
            return 1
    elif d == "upper left":
        try:  # upper left
            return graph[r+1][c-1]
        except IndexError:
            return 1
    elif d == "lower left":
        try:  # lower left
            return graph[r-1][c-1]
        except IndexError:
            return 1
    elif d == "up":
        try:  # up
            return graph[r+1][c]
        except IndexError:
            return 1
    elif d == "down":
        try:  # down
            return graph[r-1][c]
        except IndexError:
            return 1


if __name__ == "__main__":
    graph = readGrid("p011grid.txt")
    maxProduct = 0
    directions = ["right", "left", "upper right", "lower right", "upper left",
                  "lower left", "up", "down"]
    for r in range(len(graph)):
        for c in range(len(graph[r])):
            for d in directions:
                r2 = r
                c2 = c
                product = 1
                for i in range(4):
                    product *= getNextAdjacent(graph, r, c, d)
                    if d == "right":
                        c2 += 1
                    elif d == "left":
                        c2 -= 1
                    elif d == "upper right":
                        c2 += 1
                        r2 += 1
                    elif d == "upper left":
                        c2 -= 1
                        r2 += 1
                    elif d == "lower left":
                        c2 -= 1
                        r2 -= 1
                    elif d == "lower right":
                        c2 += 1
                        r2 -= 1
                    elif d == "up":
                        r2 += 1
                    else
                        r2 -= 1
                if product > maxProduct:
                    maxProduct = product
    print maxProduct
