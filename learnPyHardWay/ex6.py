binary = "binary"
do_not = "dont"

x = "There are %d types of people in this world" %10

y = "Those who know %s and those who %s" %(binary,do_not)

# printing raw data using print statement prints it with single quote
print 'I said %r' %x
# printing raw data with raw data content prints it with double quotes
print "I also said %r" %y

hilarious = False

# We are assigning a text string to a variable along with variable embedded to print any data type
joke_eval = "Isnt that joke funny? %r"

print joke_eval %hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
