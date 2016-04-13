__author__ = 'anandraj'

import datetime

day1 = datetime.date.today()

yday = datetime.timedelta(days=1)

day2 = day1 - yday

print day2

time1 = datetime.time.isoformat(datetime.time(7,53,0))

print time1

