#!/usr/bin/env python
from sys import argv,exit

def small(a,b):
    if a<b:
        return a
    else:
        return b

def main():

    while True:
        script, x,y,z = argv
        try:
            x= int(x)
            y= int(y)
            z= int(z)
            break
        except ValueError:
            print "Enter Integers only"
            exit()

    s = small(x,y)
    s = small(s,z)


    print "Smallest number from the given input", s

if __name__ == '__main__':
    main()
