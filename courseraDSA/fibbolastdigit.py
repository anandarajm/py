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
    e = (fiblist[-1]+fiblist[-2])%10
    fiblist.append(e)
    fiblist.pop(0)
print fiblist[-1]