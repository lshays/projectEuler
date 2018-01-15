i = 0
count = 0 
while count != 5:
    i += 1
    count = 0
    mySet = set()
    # Turn i into a set of its digits
    for digit in str(i):
        mySet.add(digit)

    # Loop through 2i...6i
    for n in range(2, 7):
        newSet = set()
        # Create a set of i*n's digits
        for digit in str(i*n):
            newSet.add(digit)
        # If this new set is a subset of the orignal set, increment count
        if newSet.issubset(mySet):
            count += 1
    # If count == 5, you've found your answer
    if count == 5:
        print i 
