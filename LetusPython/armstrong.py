import traceback
from sys import argv

def separate_num(num,digit):
    num_list = []
    digit -=1
    for i in range (digit,-1,-1):
        place = num/pow(10,i)
        num = num - place * pow(10,i)
        num_list.append(place)
    return num_list

def armstrong(num,num_list,length):
    arm = 0
    for i in num_list:
        arm += pow(i,length)
    if num == arm:
        return True
    else:
        return False

script , start, stop = argv

try:
    start,stop = [int(start),int(stop)]
except:
    print traceback.print_exc()
    print "Integers only"
    exit()

num_range = []
num_range.extend(range(start,(stop+1)))


print "-"*80

for i in num_range:
    length = len(str(i))
    digit_list = separate_num(i,length)
    cube = armstrong(i,digit_list,length)
    if cube:
        print "%d is a armstrong number" %i

print "-"*80