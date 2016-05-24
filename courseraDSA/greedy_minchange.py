#python2
__author__ = 'anandraj'

import sys

try:
    amt = int(sys.stdin.readline())
except:
    sys.exit()

if 1 <= amt <= 1000:
    pass
else:
    sys.exit()

tens = amt/10
amt = amt%10
fives = amt/5
amt = amt%5

print tens+fives+amt
