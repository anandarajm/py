__author__ = 'anandraj'

class students:
    def __init__(self):
        self.name = "Name"
        self.dept = "ECE"
        self.course = "B.E."
        self.yoj = 2007
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

for i in range(2):
    studlist.append(students())
i = 70
for a in studlist:
    a.name = 'banu'
    a.marks = [i+5,i,i+8,i+3]
    a.yoj+=1
    i+=1
    print a.name , a.marks , a.avg(a.marks), a.course, a.yoj , a.grade(a.avg(a.marks))

for a in studlist:
    if a.yoj == 2008:
        print a.marks
