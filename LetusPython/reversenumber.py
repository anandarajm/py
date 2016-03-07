import math

def inputcheck(num):
    n = int(math.log10(num)) + 1
    if (n != 5):
        raise StandardError()
    else:
        return

while True:
    try:
        print "Enter a 5 digit number"
        num = int(raw_input(">>>>>>"))
    except ValueError:
        print "Enter numbers only"
        continue
    try:
        inputcheck(num)
        break
    except StandardError:
        print "Enter 5 digit numbers only"

init = num
num_list = []
for i in range (4,-1,-1):
    place = num/pow(10,i)
    num = num - place * pow(10,i)
    num_list.append(place)

final = 0
for i in range (4,-1,-1):
    rev = num_list[i] * pow(10,i)
    final = final + rev

print final
if final == init:
    print "Its a palindrome of 5 digit number"
