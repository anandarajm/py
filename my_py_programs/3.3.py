rawstr = raw_input("Enter the number to grade:")
try:
    gpa = float (rawstr)
except:
    print "Please enter a number valid number"    
    quit()

# Grading logic
if gpa <= 1 and gpa >= 0.9 :
    print "A"
elif gpa <0.9 and gpa >= 0.8 :
    print "B"
elif gpa <0.8 and gpa >= 0.7 :
    print "C"
elif gpa <0.7 and gpa >= 0.6 :
    print "D"
elif gpa < 0.6 :
    print "F"
else :
    print "Please enter a number in the range 0.0 to 1.0"
