# finally files

from sys import argv

script, filename = argv
txt=open(filename)

print "Contents of the file %s" %filename
print txt.read()

txt.close()

#print txt.read()
