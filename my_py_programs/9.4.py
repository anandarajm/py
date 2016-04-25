name = raw_input("Enter file:")
if len(name) < 1 : name = "box.txt"
fh = open(name)

uid = dict()        #Unique email id counter
IDs = list()        #list of all email IDs

for line in fh :
    line = line.rstrip()
    if line.startswith('From ') :
        words = line.split()
        IDs.append(words[1])
print IDs
for id in IDs:
    uid[id]=uid.get(id,0)+1

commit = None
count = None
for key,value in uid.items():
    if count is None or value > count:
        commit = key
        count = value

print commit, count        