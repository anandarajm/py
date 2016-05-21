#python2
__author__ = 'anandraj'

import sys

def exceptionhandle():
    exctype, excvalue = sys.exc_info()[:2]
    print "We got this exception %s and the reason is %s" %(exctype.__name__,excvalue)

while True:
    try:
        # print "Enter how many numbers you want to enter"
        n = int(raw_input())
        break
    except:
        exceptionhandle()

while True:
    try:
        # print "Enter %d positive integers separated by space" %n
        usrin = sys.stdin.readline()
        numlist = usrin.split()
        if len(numlist) != n:
            raise AssertionError('not enough inputs given')
            continue
        for i in range(n):
            numlist[i]=int(numlist[i])
            if numlist[i] < 0:
                raise ValueError('negative numbers are given as input')
        break
    except:
        exceptionhandle()

numlist.sort()
product = numlist[-1]*numlist[-2]
print product



