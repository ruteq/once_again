a = 1
b = 3
c = 5

l = [a,b,c]
m1 = max(l)
print m1
l.remove(m1)
m2 = max(l)
print m2
print m1+m2

######################

price = 5000
for i in xrange(1,11):
    print i*price
######################

price = 1
start = 1.2
finish = 2
current = 1.2

while current < finish:
    print current*price
    current = current + 0.2
########################

l = [36, 56 , 67 , 658, 412, 42, 555, 668, 22, 95]

for n in l:
    #print str(n)
    s = str(n)
    if len(s)<3:
        print s
    if n == 42:
        print ('The Answer to the Ultimate Question of Life, the Universe, and Everything.')
        break
#
