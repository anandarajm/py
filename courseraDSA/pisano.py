# python2
__author__ = 'anandraj'
import sys

def fibonacci(n):
    fiblist = [0,1]
    for i in range(2,(n+1)):
        e = fiblist[i-1]+fiblist[i-2]
        fiblist.append(e)
    pisano = []
    period = 0
    for e in fiblist:
        if period == 2:
            pisano.pop()
            pisano.pop()
            break
        else:
            pisano.append(e%m)
            if pisano[-1] == 1:
                if pisano[-2] == 0:
                    period += 1
    return pisano

userin = sys.stdin.readline()
n, m = map(int, userin.split())

periodicity = pow(m,2)-1
pisano = fibonacci(periodicity)
print pisano , len(pisano)

