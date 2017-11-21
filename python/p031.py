# How many different ways can 200p be made using any number of coins?
# Values are 1p, 2p, 5p, 10p, 20p, 50p, 1 (100p) and 2 (200p).


# Saw this algorithm on stackoverflow :(
def coinCombos(coins, goal):
    if goal == 0:
        return 1
    elif goal < 0 or not any(coins):
        return 0
    else:
        return coinCombos(coins, goal-max(coins)) + coinCombos(coins[0:-1], goal)


if __name__ == "__main__":
    print coinCombos([1, 2, 5, 10, 20, 50, 100, 200], 200)
