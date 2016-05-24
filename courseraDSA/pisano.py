# python2
__author__ = 'anandraj'
import sys

def fibonacci(n):
    fiblist = [0,1]
    period=0
    for i in range(2,(n*100)):
        if period == 1:
            fiblist.pop()
            fiblist.pop()
            break
        else:
            e = (fiblist[i-1]+fiblist[i-2])%n
            fiblist.append(e)
            if fiblist[-1] == 1:
                if fiblist[-2] == 0:
                    period += 1
    return fiblist

userin = sys.stdin.readline()
n, m = map(int, userin.split())

pisano = fibonacci(m)
l = len(pisano)
# print pisano, l
index = n % l
print pisano[index]
