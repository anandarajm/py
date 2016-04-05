def fibbo(n):
    a = 0
    b=1
    for i in range(n):
        s = a + b
        a = b
        b=s
    return b

c1 = 1
c2 = 1

for i in range(50):
    print fibbo(i),
    if c1 == c2:
        print ""
        c2=0
        c1+=1
    c2+=1



