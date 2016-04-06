import argparse

parser = argparse.ArgumentParser()
parser.add_argument("t",type=int,help='Table of what number')
parser.add_argument("n",type=int,help='Table upto \'n\' times')
args=parser.parse_args()

for i in range (1,args.n+1):
    print "%d * %d = %d" %(args.t,i,(args.t*i))