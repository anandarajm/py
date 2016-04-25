raw = raw_input ("Enter total working hours:")
try:
    hours = float(raw)
except:
    print " Enter valid number for hours"
    quit()
raw = raw_input ("Enter pay rate:")
try:
    rate = float(raw)
except:
    print " Enter a valid number for rate"
    quit()
if hours <= 40:
    pay = hours * rate
else :
    ot = hours - 40
    pay = (40 * rate) + (ot * rate * 1.5)
print pay
