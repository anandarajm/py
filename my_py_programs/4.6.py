# Function computepay
def computepay(h,r):
    if h <= 40:
        pay = hours * rate
        return pay
    else :
        ot = hours - 40
        pay = (40 * rate) + (ot * rate * 1.5)
        return pay

# Main program
#getting input
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

#Function call
print computepay(hours,rate)