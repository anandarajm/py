people = 30
cars = 2
trucks = 5

if cars > people:
    print "We have more cars"
elif cars < people:
    print "cars are less than number of people"
else:
    print "Looks like we have equal number of cars and people"

if trucks > cars:
    print "Too many trucks :O"
elif trucks < cars:
    print "less trucks more cars"
else:
    print "looks like we equal cars and trucks"

if people > trucks or cars < trucks:
    print "more people less trucks"
else:
    print "Lot of trucks!"
