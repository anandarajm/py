while True:
    try:
        print "Enter total number of hours worked"
        total_time = int(raw_input(">>>"))
        break
    except ValueError:
        print "Enter integers only"
        continue

#adding comment line in conflict branch
ot = total_time - 40


if ot < 0: #comment
    print "Employee hasnt worked over time"
else:
    ot_pay = ot*12
    print "Overtime pay %d" %ot_pay

while ot > 0:
    ot_pay = ot*12
    print "Overtime pay %d" %ot_pay
    break
