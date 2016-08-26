import sys

n1 = 0
n2 = 1
i = 1
my_list = []
my_list.insert(0,n1)
my_list.insert(1,n2)

print "This program will print fibonacci series upto n values, give value of n"

while True:
    try:
        x = raw_input(">>>>")
        x = int(x)
        break
    except:
        print "You should enter the value only in numbers"


while i < (x-1):
    n = n1 + n2
    n1 = n2
    n2 = n
    my_list.append(n)
    i=i+1


for n in my_list:
    print n