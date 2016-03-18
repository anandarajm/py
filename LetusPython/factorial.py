from sys import argv

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