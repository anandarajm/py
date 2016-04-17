def add(n):
    sum = 0
    if n > 0:
        sum = n+add(n-1)
    return sum

def printfibbo(n):
    if n == 0 or n == 1:
        return n
    else:
        s = printfibbo(n-1) + printfibbo(n-2)
        return s

def binary(n):
    if n ==0:
        return 0
    elif n > 0:
        return str(binary(n/2)) + str(n%2)

if __name__ == '__main__':
    s = add(20)
    print s
    for i in range(20):
        f = printfibbo(i)
        print f ,
    print

    b = binary(15)
    print b
    Matrix = [[x for x in range(5)] for x in range(5)]
    print Matrix
    print Matrix[1][1]
    