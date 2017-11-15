dictOnes = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
}

dictTens = {
        00: "",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
}


# Assumes n is a string
def translateNumber(n):
    if len(n) == 4:
        return "OneThousand"
    elif len(n) == 3:
        value = dictOnes[int(n[0])] + "hundred"
        if n[1] == "0" and n[2] == "0":
            return value
        else:
            return value + "and" + translateNumber(n[1:])
    elif len(n) == 2:
        if n[0] == "1":
            return dictTens[int(n)]
        else:
            return dictTens[int(n[0] + "0")] + translateNumber(n[1])
    else:
        return dictOnes[int(n)]


if __name__ == "__main__":
    sum = 0
    for i in range(1, 1001):
        sum += len(translateNumber(str(i)))
    print sum
