l = [5, 10, 13, 15, 26, 32, 39, 40]
l2 = []
for n in l:

    if n % 13 != 0:
       # print n
        continue
    else:
        l2.append(n)
print l2

