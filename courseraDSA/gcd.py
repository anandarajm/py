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
    return l[0]

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int,input.split())
    print gcd(a,b)