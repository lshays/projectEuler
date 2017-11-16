# Sort the list of names in p022.txt in alphabetical order
# Then for each name in the list, find its letter score,
# and multiply it by its position in the list. Sum all of these.


# ASCII value for 'a' is 97
# ASCII(letter) - 96 gives individual letter scores
def getLetterScore(name):
    score = 0
    for letter in name.lower():
        score += ord(letter) - 96
    return score


if __name__ == "__main__":
    nameList = []
    with open("p022.txt", 'r') as file:
        for name in file.read().replace('"', '').strip().split(","):
            nameList.append(name)
    nameList.sort()
    sum = 0
    for i in range(len(nameList)):
        sum += (i+1) * getLetterScore(nameList[i])
    print sum
