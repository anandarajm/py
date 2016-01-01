import datetime
date=datetime.datetime.now()

class song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics


    def words(self):
        for word in self.lyrics:
            print word

year = song(["Happy", "new", "year",date.year])
year.words()



today = date.day , date.month
print today

day = song(["Happy birthday to", today , "born"])
day.words()
