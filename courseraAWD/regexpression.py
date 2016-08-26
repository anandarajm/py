import re

fh = open('regexpsum.txt','r')

print sum(map(int,re.findall(r'[0-9]+',fh.read())))
