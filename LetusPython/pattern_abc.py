alpha = map(chr,(range(ord('A'),(ord('D')+1))))
l1 = alpha[:]
alpha.reverse()
l2 = alpha

empty = []
d=0

size = len(l1)
print size


for i in range(size,-1,-1):
    for j in range(0,i):
        print l1[j],
    for j in range(0,len(empty)):
        print empty[j],
    for j in range(0,i):
        print l2[(j+d)],
    if d < size:
        d+=1
        empty.append("   ")
        print ""

for i in range(0,(size+1)):
    for j in range(0,i):
        print l1[j],
    for j in range(0,len(empty)):
        print empty[j],
    for j in range(0,i):
        print l2[(j+d)],
    d-=1
    if i < (size):
        empty.remove("   ")
        print ""