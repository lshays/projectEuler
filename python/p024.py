# What is the millionth lexicographic permutation i
# of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import sys

counter = 0
mystring = "0123456789"
for a in mystring:
    for b in mystring.replace(a, ""):
        for c in mystring.replace(a, "").replace(b, ""):
            for d in mystring.replace(a, "").replace(b, "").replace(c, ""):
                for e in mystring.replace(a, "").replace(b, "").replace(c, "").replace(d, ""):
                    for f in mystring.replace(a, "").replace(b, "").replace(c, "").replace(d, "").replace(e, ""):
                        for g in mystring.replace(a, "").replace(b, "").replace(c, "").replace(d, "").replace(e, "").replace(f, ""):
                            for h in mystring.replace(a, "").replace(b, "").replace(c, "").replace(d, "").replace(e, "").replace(f, "").replace(g, ""):
                                for i in mystring.replace(a, "").replace(b, "").replace(c, "").replace(d, "").replace(e, "").replace(f, "").replace(g, "").replace(h, ""):
                                    for j in mystring.replace(a, "").replace(b, "").replace(c, "").replace(d, "").replace(e, "").replace(f, "").replace(g, "").replace(h, "").replace(i, ""):
                                        counter += 1
                                        if counter == 1000000:
                                            print a+b+c+d+e+f+g+h+i+j
                                            sys.exit()
