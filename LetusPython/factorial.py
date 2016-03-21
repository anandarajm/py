from sys import argv
import math

script, n = argv

try:
    n = int(n)
except:
    exit()
fact = 1
while n > 1:
    fact = fact * n
    n = n-1

print fact
print math.factorial(n)