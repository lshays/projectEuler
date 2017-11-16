# How many Sundays fell on the first of the month between Jan 1, 1901, and Dec 31, 2000?
# Jan 1, 1900 was a Monday
# Leap years occur on years divisible by 4, but not century years unless divisible by 400


def isLeapYear(n):
    return n % 4 == 0 and (n % 100 != 0 or n % 400 == 0)


if __name__ == "__main__":
    year = 1900
    sunday = 7
    total = 0
    while year < 2001:
        firsts = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
        days = 365
        if isLeapYear(year):
            days += 1
            firsts = [d+1 for d in firsts]
            firsts[0] = 1
            firsts[1] = 32
        while sunday <= days:
            if sunday in firsts and year > 1900:
                total += 1
            sunday += 7
        sunday = sunday - days
        year += 1
    print total
