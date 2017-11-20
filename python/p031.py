# How many different ways can £2 be made using any number of coins?
# Values are 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

coins = [1, 2, 5, 10, 20, 50, 100, 200]
coinCounts = [200/c for c in coins]
solutions = 0


# Gives coin combos that add to goal using
# at least one of max(coins)
def coinCombos(coins, goal):
