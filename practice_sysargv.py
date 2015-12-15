import sys
print sys.argv [1:]

l = sys.argv [1:]
l2 = []
for s in l:
    number = int(s)
    l2.append(number)
print l2
print sum (l2)
