fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "box.txt"

fh = open(fname)
count = 0
emailid = list()
for line in fh :
    line = line.rstrip()
    if line.startswith('From ') :
        words = line.split()
        print words[1]
        emailid.append(words[1])
count = len(emailid)         
        
print "There were", count, "lines in the file with From as the first word"
