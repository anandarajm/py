#python2
import sys

def getmax(capacity, n, value, weight):
    maxwt = 0
    maxval = 0
    prop = []
    limit = capacity

    for i in range(0,n):
        prop.append(value[i]/float(weight[i]))

    propsort = sorted(range(len(prop)), key = lambda k: prop[k], reverse=True)
    # print prop, propsort

    for i in propsort:
        if limit == maxwt:
            pass
        else:
            if capacity-weight[i] >= 0:
                tempwt = weight[i]
            else:
                tempwt = capacity

            maxval = maxval+tempwt*prop[i]
            maxwt = maxwt+tempwt
            capacity = capacity - tempwt
            # print ">>>>" , maxval, maxwt, capacity, weight[i], limit

    return maxval


if __name__ == "__main__":
    data = list(map(int, (sys.stdin.readline().split())))
    n,capacity = data[0:2]
    value = []
    weight = []
    for i in range(n):
        data = list(map(int, (sys.stdin.readline().split())))
        v, w = data[0:2]
        value.append(v)
        weight.append(w)
    maxvalue = getmax(capacity,n,value,weight)
    print "%.10f"  %maxvalue
