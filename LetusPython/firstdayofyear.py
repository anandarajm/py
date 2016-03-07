import datetime
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def inputcheck(num):
    if (num < 0):
        raise StandardError()
    else:
        return

while True:
    try:
        print "Enter any year after 1900"
        year = int(raw_input(">>>"))-1900
    except ValueError:
        print "Enter a valid number"
    try:
        inputcheck(year)
        break
    except StandardError:
        print "Year should be greater than 1900"

leaplogic = (((year-1)/4)%7)
day = ((year+leaplogic) % 7)

print day
print "First day of year %d is %s" %((year+1900), days[day])

print "*"*80
moddate = datetime.date(year,1,1).weekday()
print moddate