

counter = [0,1,2,3,4,5,6,7,8,9]
fruits =["apple","banana","cherry","lemon","pear","orange"]
change = [1,'pennies',2,'nickel',3,'dime',4,'quarter']

for number in counter:
    print "single digit numbers are %d" %number

for fruit in fruits:
    print "The fruit I regularly eat are", fruit

# Lists are type aganostic, we could parse different data types

for elements in change:
    print "I have following type of coins in different numbers %s", elements

test_list = []
print 'creating a list with 10 elements in space of 10'
for i in range(0,100,10):
    print 'list contents', test_list
    list_count = len(test_list)
    print 'parsing the list elements with %d elements' %list_count
    for x in test_list:
        print x
    test_list.append(i)


print "final list content", test_list