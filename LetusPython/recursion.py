__author__ = 'anandraj'

def fact(x):
    if x==1:
        return 1
    else:
        f = x*fact(x-1)
    return f

def fibbo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibbo(n-1)+fibbo(n-2)

if __name__=='__main__':
     out = fact(5)
     print out
fib = []
for i in range(1,20):
    fib.append(fibbo(i))
fib.insert(0,0)
print fib