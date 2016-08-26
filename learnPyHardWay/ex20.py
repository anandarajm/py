from sys import argv

script, in_file, n = argv

def print_all(handle):
    print handle.read()

def rewind(handle):
    handle.seek(0)

def print_line(line,handle):
    print line, handle.readline()

fh = open(in_file)
print_all(fh)

print "Seeking back to beginning of the file"
rewind(fh)

n=int(n)
for i in range (0,n):
    print_line(i,fh)
    
