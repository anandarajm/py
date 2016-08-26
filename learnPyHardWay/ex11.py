# lets ask questions

while True:
    try:
        age = int(raw_input("What's your age:"))
        break
    except ValueError:
        print "Input for age should an integer value"
        
print " What is your height?"
h = raw_input()

print " What is your weight?"
w = raw_input()

print '''Anandraj's is %r old, he is %r cm tall and weighs %r kg. 
         He is learning to program only now !!! :( :) ''' %(age, h, w)
