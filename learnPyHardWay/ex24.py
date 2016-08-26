import datetime

print "Lets revise everything"
print "I now know about \\ character. It helps intro spl print statements like \n new line and \t tabs"

mandhiram = """
thanam tharum kalvi tharum oru naalum thalarvu ariya manam tharum 
nenjil vanjam illa inam tharum , nallanavellam tharum
anbar enbavarke ganam tharum poonguzhalaal abhiraamiyin kadai kangale"""

print "-"*80
print mandhiram
print "-"*80                

# some random function with multiple reutrn statements"

def multi_ret(arg):
    square = arg * arg
    cube = arg * arg * arg
    exp10 = arg ** 10
    return square, cube, exp10

x = datetime.datetime.now()
date = x.day
sq , cu , ex = multi_ret(date)

print """We are going to manipulate today's date %d, square of it %d
cube of it %d and multiplied by exponential 10 times %d """ %(date,sq,cu,ex)


