def greatestAdjacent(graph, r, c):
    max = 0
    try:  # right
        if graph[r][c+1] > max:
            max = graph[r][c+1]
    except IndexError:
        pass
    try:  # left
        if graph[r][c-1] > max:
            max = graph[r][c-1]
    except IndexError:
        pass
    try:  # upper right
        if graph[r+1][c+1] > max:
            max = graph[r+1][c+1]
    except IndexError:
        pass
    try:  # lower right
        if graph[r-1][c+1] > max:
            max = graph[r-1][c+1]
    except IndexError:
        pass
    try:  # upper left
        if graph[r+1][c-1] > max:
            max = graph[r+1][c-1]
    except IndexError:
        pass
    try:  # lower left
        if graph[r-1][c-1] > max:
            max = graph[r-1][c-1]
    except IndexError:
        pass
    try:  # up
        if graph[r+1][c] > max:
            max = graph[r+1][c]
    except IndexError:
        pass
    try:  # down
        if graph[r-1][c] > max:
            max = graph[r-1][c]
    except IndexError:
        pass

