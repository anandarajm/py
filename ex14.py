from sys import argv

script, user = argv
prompt = 'edavudhu sollu>'

print "%s is learning python" %user
print "Is %s regularly doing the exercises?" %user
regular= raw_input(prompt)

print "%s is saying he is doing the exercises %r" %(user, regular)
