# Finds the smallest positive integer that is evenly divisible by all numbers 1-20
def lowestCommonMultiple():
    tester = 20
    nums = range(10,21)
    while True:
        for num in nums:
            if tester % num != 0:
                tester += 20
                break
            if num == 20:
                return tester

if __name__ == "__main__":
    print lowestCommonMultiple()
