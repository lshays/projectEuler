# What is the index of the first fib number to contain 1000 digits?


def fibgen(f1, f2):
    while(True):
        f3 = f1 + f2
        yield f3
        f1 = f2
        f2 = f3


if __name__ == "__main__":
    gen = fibgen(1, 1)
    index = 3
    while len(str(next(gen))) != 1000:
        index += 1
    print index
