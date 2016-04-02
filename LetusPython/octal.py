while True:
    try:
        print "Enter a number to convert to Octal number"
        num = int(raw_input(">>>>>>"))
        break
    except ValueError:
        print "Enter numbers only"
        continue

print oct(num)
print "&"*80

octal = ''

while num > 8:
    q = num/8
    r = num%8
    octal = str(r)+octal
    num = q
    print octal
octal = str(q) + octal

print q,r, octal