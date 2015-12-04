from sys import argv

script, filename = argv 

prompt  = ">>>"

print "We are going to mess around with the file %s" %filename
print "So shall we start messing around?"
raw_input(prompt)

obj     = open(filename, 'w')

print "file contents are going to be erased"
obj.truncate()

# Note after truncating a file, you need to reopen the file to read  
# the contents of the file. 
print "Lets add new contents to the file"
w1=raw_input("W1 ")
w2=raw_input("W2 ")
w3=raw_input("W3 ")

obj.write(w1)
obj.write("\n")
obj.write(w2)
obj.write("\n")
obj.write(w3)
obj.write("\n")

w = "\n".join([w1,w2,w3])
obj.write (w)

obj = open(filename)
print obj.read()*3

obj.close()
