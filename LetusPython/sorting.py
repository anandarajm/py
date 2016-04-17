__author__ = 'anandraj'

import time
import random

def selection_sort(numlist):
    for j in range(len(numlist)):
        for i in (range(j,len(numlist))):
            if numlist[j] > numlist[i]:
                temp = numlist[i]
                numlist[i]=numlist[j]
                numlist[j]=temp
    return numlist

def bubble_sort(numlist):
    for i in range(len(numlist)):
        for j in range (len(numlist)):
            if numlist[j]>numlist[i]:
                temp = numlist[i]
                numlist[i]=numlist[j]
                numlist[j]=temp
                # print "Iteration Outer loop %d - Inner loop - %d - %s" %(i,j,numlist)
    return numlist

def insertion_sort(numlist):
    for i in range(len(numlist)):
        for j in range(i):
            if numlist[j]>numlist[i]:
                temp = numlist[i]
                numlist[i]=numlist[j]
                numlist[j]=temp
                # print "Iteration Outer loop %d - Inner loop - %d - %s" %(i,j,numlist)
    return numlist

if __name__ == '__main__':
    numbers = []
    for i in range(15):
        numbers.append(random.randint(1,10000))
    random.shuffle(numbers)
    print "After shuffling", numbers
    mylist = numbers[:]
    t1 = time.clock()
    sortedlist = selection_sort(mylist)
    t2 = time.clock()
    diff = t2 - t1
    print "Sorting using selection sort - %s & time taken to sort %f" %(sortedlist,diff)
    mylist = numbers[:]
    t1 = time.clock()
    sortedlist = bubble_sort(mylist)
    t2 = time.clock()
    diff = t2 - t1
    print "Sorting using bubble sort - %s & time taken to sort %f" %(sortedlist,diff)
    mylist = numbers[:]
    t1 = time.clock()
    sortedlist = insertion_sort(mylist)
    t2 = time.clock()
    diff = t2 - t1
    print "Sorting using insertion sort - %s & time taken to sort %f" %(sortedlist,diff)
    mylist = numbers[:]
    t1 = time.clock()
    mylist.sort()
    t2 = time.clock()
    diff = t2 - t1
    print "Sorting using inbuilt sort - %s & time taken to sort %f" %(mylist,diff)