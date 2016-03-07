from sys import argv

script, year =  argv
while True:
    try:
        year = int(year)
        break
    except ValueError:
        print "Enter a proper integer"


if (year%4==0):
    print "Its a leap year"
else:
    print "Its not a leap year"