__author__ = 'anandraj'


def avg (marks):
    n = len(marks)
    t = float(sum(marks))
    return t/n

def get_avg(dict):
    hw = avg(dict['homework'])
    qu = avg(dict['quizzes'])
    te = avg(dict['tests'])
    return hw*.1 + qu*.3 + te*.6

def grade_sys(num):
    if num >= 90: return 'A'
    elif num >= 80: return 'B'
    elif num >= 70: return 'C'
    elif num >= 60: return 'D'
    else: return 'F'

lloyd = {
  "name": "Lloyd",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd,alice,tyler]
for student in students:
    print 'name ---', student['name']
    for key, value in student.iteritems():
        if not key == 'name':
            print key ,'---', value
    print '*'*80

for student in students:
    print "Weighted Average of %s - %f" %(student['name'], get_avg(student))
    student['wt_avg'] = get_avg(student)
    print "Grade of %s - %c" %(student['name'],grade_sys(student['wt_avg']))

list_avg = []
for student in students:
    list_avg.append(student['wt_avg'])

class_avg = avg(list_avg)

print class_avg

print "Grade of the class - %c" %grade_sys(class_avg)