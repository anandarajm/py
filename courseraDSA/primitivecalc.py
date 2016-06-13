#python2

import sys

d = {}

def f(n):
    if n == 1:
        return 1, -1
    if d.get(n) is not None:
        return d[n]
    ans = (f(n - 1)[0] + 1, n - 1)

    if n % 2 == 0:
        ret = f(n // 2)
        if ans[0] > ret[0]:
            ans = (ret[0] + 1, n // 2)

    if n % 3 == 0:
        ret = f(n // 3)
        if ans[0] > ret[0]:
            ans = (ret[0] + 1, n // 3)

    d[n] = ans
    return ans

def print_solution(n):
    print (f(n)[0]-1)
    ans = []
    while f(n)[1] != -1:
        ans.append(n)
        n = f(n)[1]
        # print n
    ans.append(1)
    ans.reverse()
    for x in ans:
        print x,


if __name__=='__main__':
    num = sys.stdin.readline().split()
    n = int(num[0])
for i in range(1, n):
    f(i)[0]
print_solution(n)
print ''
