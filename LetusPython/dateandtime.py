__author__ = 'anandraj'

import time
import calendar
import datetime


# time in epoch

a = time.time()
print a
# time in structure of day date time etc
b = time.localtime(time.time())
print b
# time in human readable format
c = time.asctime(b)
print c

# print current time easy way
d = time.ctime()
print d

# time taken by the program to run
e = time.clock()
print e

# print the UTC time
print time.gmtime()

# converts stucture back to float
print time.mktime(b)

# prints time zone name
print time.tzname

# prints UTC time in readable format
print time.asctime(time.gmtime())

# prints timezone offset in seconds from UTC without DST
print time.altzone

# Library datetime helps work with date/time/datetime classes

print datetime.time.__doc__
print datetime.date.__doc__
print datetime.datetime.__doc__


print datetime.time(1,40,0)

print datetime.datetime(2016,2,29,22,12,1)

print datetime.date(2018,6,14)

t = datetime.date(2040,1,1)
#prints path of the given library
print datetime.__file__

print calendar.TextCalendar(calendar.SUNDAY).formatyear(2016,1,1,3,3)
