import re

fh = open('regexpsum.txt','r')

x =  sum(map(int,re.findall(r'[0-9]+',fh.read())))

print x

if x/2==0:
	print "Even"
else:
	print "odd"

