things = "laptop harddisk mouse cup bag note box"

stuff = things.split(" ")
more_stuff = ["bed", "pillow", "purse", "kerchief"]

while len(stuff) < 10:
    new_stuff = more_stuff.pop()
    print new_stuff
    stuff.append(new_stuff)
    print "Now we have %d items in list stuff" %len(stuff)

print "Now the list stuff has following elements"
print stuff


print "Return last item in the list -   ", stuff.pop()
print "Printing list elements with a single print statement"
print "Things around me are ", '^'.join(stuff[3:6])