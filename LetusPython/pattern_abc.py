alpha = map(chr,(range(ord('A'),ord('N'))))
l1 = alpha[:]
alpha.reverse()
l2 = alpha

empty = []
d=0

size = len(l1)

for i in range(size,0,-1):
    for j in range(0,i):
        print l1[j],
    for j in range(0,len(empty)):
        print empty[j],
    for j in range(0,i):
        print l2[(j+d)],
    d+=1
    empty.append("   ")
    print ""
