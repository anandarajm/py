# this function takes multiple arguments with *args similar to argv

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1, arg2)
    
# get two arguments and pass it to the function (traditional)

def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" %(arg1, arg2)
    
 # take one agrument using *args
 
def print_one(*args):
    one=args
    print "argument: %r" %one

def zero_arg():
    print "No arguments were passed to this function"
        
print_two("Anand","Banu")
print_two_again ("Raj","Priya")
print_one("Oct")
zero_arg()
