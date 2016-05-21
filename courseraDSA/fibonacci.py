#python2
import sys

try:
    n=int(raw_input())
except:
    print "Enter integers only"

# if 0 <= n <= 45:
#     pass
# else:
#     sys.exit()

fiblist = [0,1]
for i in range(2,(n+1)):
    e = fiblist[i-1]+fiblist[i-2]
    fiblist.append(e)
print fiblist[n]
