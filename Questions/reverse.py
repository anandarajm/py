import string

alphabets = string.lowercase[:]
alphalist = []
revlist = []
for alpha in alphabets:
    alphalist.append(alpha)
    revlist.append(alpha)
revlist.reverse()
sentence = 'xyz'
revsent = None

for s in sentence:
    pos = alphalist.index(s)
    print revlist[pos]