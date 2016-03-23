import traceback
from optparse import OptionParser
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
    if length == 1:
        return False
    else:
        arm = 0
        for i in num_list:
            arm += pow(i,length)
        if num == arm:
            return True
        else:
            return False

#script , start, stop = argv



usage = "usage: %prog -b <int> -e <int>"
parser = OptionParser(usage=usage)
parser.add_option("-b", dest="begin",
                  help="Starting range to find Armstrong number", type="int")
parser.add_option("-e", dest="end",
                  help="Ending range to find Armstrong number", type="int")

(options, args) = parser.parse_args()
print "----" %args
'''
try:
    start,stop = [int(start),int(stop)]
except:
    print traceback.print_exc()
    print "Integers only"
    exit()
'''
num_range = []
num_range.extend(range(options.begin,(options.end+1)))


print "-"*80

for i in num_range:
    length = len(str(i))
    digit_list = separate_num(i,length)
    cube = armstrong(i,digit_list,length)
    if cube:
        print "%d is a armstrong number" %i

print "-"*80