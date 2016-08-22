from sys import argv
from os.path import exists
import shutil


script, from_f, to_f = argv

print "Copying contents of %s to %s" %(from_f, to_f)

'''
fh_in = open(from_f, 'r')
fh_out = open(to_f, 'w+')
data = fh_in.read()
fh_out.truncate()

print "Size of the file in bytes = " , len(from_f)

print "does the destination file exists? %r" %exists(to_f)



print "Contents of file %s before writing" %to_f
print fh_out.read()
fh_out.write(data)
print "Contents of file %s after writing" %to_f

fh_out = open(to_f)
print fh_out.read()

fh_in.close()
fh_out.close()
'''

shutil.copyfile(from_f,to_f)
print "Contents of file %s after writing" %to_f

fh_out = open(to_f)
print fh_out.read()

