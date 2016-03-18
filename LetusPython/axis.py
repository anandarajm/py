import traceback
import sys

while True:
    try:
        print "Enter co-ordinage %d numbers in format a b"
        x,y = raw_input(">>>").split()
        x,y = [int(x),int(y)]
        break
    except:
        print traceback.print_exc()
        print "Integers only"

if x==0 and y==0:
    print "The origin"
elif x==0:
    print "The coordinate is in x axis"
elif y==0:
    print "The coordinate is in y axis"
else:
    print "Somewhere in the graph, not in any axis"