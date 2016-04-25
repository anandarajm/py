__author__ = 'anandraj'

import random

mylist = [random.randint(-20,20) for x in range(25)]

print mylist

num = 12

if num in mylist:
    print "Number of times number %d is present in the given list is %d" %(num,mylist.count(num))

negnum = postnum = odd = even = 0

for n in mylist:
    if n<0:
        negnum+=1
    else:
        postnum +=1
    if n%2 == 0:
        even +=1
    else:
        odd +=1

print "Negative numbers %d \nPositive numbers %d \nOdd numbers %d \nEven numbers %d" %(negnum,postnum,odd,even)

list1 = [x for x in range(2,100)]

lo_index = 0
for i in list1:
    if i ==2 or i==3 or i==5  or i==7:
        pass
    elif i%2 == 0 or i%3 ==0 or i%5 ==0 or i%7==0:
        list1[lo_index] = 0
    lo_index+=1
prime = []
for i in list1:
    if i:
        prime.append(i)

revprime = prime[:]
revprime.reverse()
print revprime
print min(revprime)

list2 = [[i for i in range(5)] for j in range(10,5,-1)]
print list2, list2[0][4], list2[3][2]
list2.append(999)
print max(max(list2))