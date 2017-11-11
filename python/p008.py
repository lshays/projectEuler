# Find the 13 adjacent digits that have the greatest product.
# What is that product?
# p008numbers.txt contains the numbers to be used for this problem


def getString():
    with open("p008numbers.txt", 'r') as file:
        myString = ""
        for line in file.read():
            myString += line.strip()
        return myString


# Returns the max product of (length) adjacent numbers
# in the string, numbers
def maxProductAdjacent(numbers, length):
    maxProduct = 0
    for i in range(len(numbers)-length+1):
        localMax = int(numbers[i])
        for j in range(1, length):
            localMax *= int(numbers[i+j])
        if localMax > maxProduct:
            maxProduct = localMax
    return maxProduct


if __name__ == "__main__":
    numberString = getString()
    print maxProductAdjacent(numberString, 13)
