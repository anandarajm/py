import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("r",help="Enter the range to find the sum of factorial series", type=int)
args=parser.parse_args()
sum = 0
sum = float(sum)
for i in range(1,(args.r+1),1):
    i= float(i)
    sum = sum + (i/math.factorial(i))
    print sum,math.factorial(i)

