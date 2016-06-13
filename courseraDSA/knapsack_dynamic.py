#python2
import sys

# def getmax(capacity, weight):
#     weight.sort()
#     bag = {}
#     for i in range(1,(capacity+1)):
#         for j in range(len(weight)):
#             k = str(i)+str(j)
#             bag.get(k,0)
#             bag[k]=0
#             wt=weight[:j+1]
#             if min(wt) < i:
#
#
#             print k, bag[k], w , wt
#
#     return max(bag.values())

def optimal_weight(W, wt):
    """Find max weight that can fit in knapsack size W."""
    # Create n nested arrays of 0 * (W + 1)
    max_vals = [[0] * (W + 1) for x in range(len(wt))]
    # Set max_vals[0] to wt[0] if wt[0] <= j
    max_vals[0] = [wt[0] if wt[0] <= j else 0 for j in range(W + 1)]
    for i in range(1, len(wt)):
        for j in range(1, W + 1):
            value = max_vals[i - 1][j]  # previous i @ same j
            if wt[i] <= j:
                val = (max_vals[i - 1][j - wt[i]]) + wt[i]
                if value < val:
                    value = val
                    max_vals[i][j] = value
                else:
                    max_vals[i][j] = value  # set to [i - 1][j]
            else:
                max_vals[i][j] = value  # set to [i - 1][j]

    return max_vals[-1][-1]

if __name__ == "__main__":
    data = list(map(int, (sys.stdin.readline().split())))
    capacity,n = data[0:2]
    weight = list(map(int, (sys.stdin.readline().split())))

    print optimal_weight(capacity,weight)


