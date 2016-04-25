largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    if len(num) < 1 : continue
    try:
        x = int(num)
    except:
        print "Invalid input"
        continue
    # Logic for Smallest
    if smallest is None:
        smallest = x 
    elif x < smallest:
        smallest = x
    # Logic for largest
    if largest is None:
        largest = x
    elif x > largest:
        largest = x
    

print "Maximum", largest
print "Minimum", smallest