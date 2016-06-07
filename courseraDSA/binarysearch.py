#python2

import sys

def binary_search(a,start, stop, x):

    if x < a[start] or x > a[stop]:
        return -1
    mid = (start + (stop-start)/2)
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary_search(a,start,mid-1,x)
    else:
        return binary_search(a, mid+1, stop, x)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = list(map(int, (sys.stdin.readline().split())))
    data = list(map(int, (sys.stdin.readline().split())))

    n = input[0]
    a = input[1:]
    k = data[0]
    b = data[1:]

    for x in b:
        # replace with the call to binary_search when implemented
        # print linear_search(a, x),
        print binary_search(a,0,(n-1),x),
