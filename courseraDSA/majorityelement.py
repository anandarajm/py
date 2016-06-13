#python2
import sys

def find_majority(data,n):
    count = {}
    for i in data:
        count[i] = count.get(i,0)+1
    d =  max(count.values())
    if d > (n/2):
        return 1
    else:
        return 0

if __name__=='__main__':
    val = map(int,sys.stdin.readline().split())
    data = list(map(int, (sys.stdin.readline().split())))
    n = val[0]
    if len(data) != n:
        sys.exit()
    print find_majority(data,n)