while True:
    try:
        print "Enter Length of rectangle"
        l = float(raw_input(">>>"))
        print "Enter Breadth of rectangle"
        b = float(raw_input(">>>"))
        break
    except:
        print "Enter numbers only"

# area = l * b
a = l * b

#Perimeter = 2(l+b)
p = 2*(l+b)

if a > p:
    print "Area is bigger"
else:
    print "Perimeter is bigger"