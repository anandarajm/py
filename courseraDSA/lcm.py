#python2
__author__ = 'anandraj'

import sys

def gcd(x,y):
    l=[]
    l.append(x)
    l.append(y)
    while l[1]:
        temp = l[:]
        l[0] = l[1]
        l[1] = temp[0]%temp[1]
        # print l
        # if l[1] == 0:
        #     print "Gcd is",l[0]
    return l[0]

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int,input.split())
    g = gcd(a,b)
    p = a*b
    l = p/g
    print l