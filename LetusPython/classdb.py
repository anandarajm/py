__author__ = 'anandraj'

class students:
    def __init__(self):
        self.name = "Name"
        self.dept = "ECE"
        self.course = "B.E."
        self.yoj = "2007"
        self.marks = []
    def avg(self,marks):
        return sum(self.marks)/len(self.marks)
    def grade(self,avg):
        if avg > 90:
            return "S"
        elif avg > 80:
            return "A"
        elif avg > 70:
            return "B"
        elif avg > 60:
            return "C"
        else:
            return "D"

studlist = []

for i in range(25):
    studlist.append('a'+str(i))
i = 70
for a in studlist:
    a = students()
    a.name = 'banu'
    a.marks = [i+5,i,i+8,i+3]
    i+=1
    # print a.name , a.marks , a.avg(a.marks), a.course, a.yoj , a.grade(a.avg(a.marks)), type(a)
    print type(a)

for a in studlist:
    print type(a)