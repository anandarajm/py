import traceback
import sys

x=[None]*3
y=[None]*3
while True:
    try:
        for i in range(0,3,1):
            print "Enter co-ordinage %d numbers in format a b" %i
            x[i],y[i] = raw_input(">>>").split()
            x[i],y[i] = [int(x[i]), int(y[i])]
        break
    except:
        print traceback.print_exc(file="exception.log")
        print "Integers only"


def straight(l):
    return all(point == l[0] for point in l)

if straight(x) or straight(y):
    print "The given co-ordinates are in a straight line"
else:
    print "The given co-ordinates don't form a straight line"
