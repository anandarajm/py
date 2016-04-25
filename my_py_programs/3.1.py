raw = raw_input ("Enter total working hours:")
hours = float(raw)
raw = raw_input ("Enter pay rate:")
rate = float(raw)
if hours <= 40:
    pay = hours * rate
else :
    ot = hours - 40
    pay = (40 * rate) + (ot * rate * 1.5)
print pay
