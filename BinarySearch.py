""" reset, resets basic op counter to 0 """
import math
numOps = 0


def reset():
    global numOps
    numOps = 0

""" basicOps returns the number of basic operations """
def basicOps():
    global numOps
    return numOps

def binarySearch(items, left, right, x):
    global numOps
    items.sort()

    if left > right:
        return -1
    
    else:
        mid = (right + left)//2
        numOps +=1

        if x == items[mid]:
            return mid
        
        elif x > items[mid]:
            numOps += 1
            return binarySearch(items, mid+1, right, x)

        else:
            numOps += 1
            return binarySearch(items, left, mid-1, x)

""" 
    avgBasicOpsFullTree, for a binary tree of size n, this function 
    returns the average number of basic operations as a double

    For calculation of expected average number of basic operations, assume:
        1.  each integer value contained in the binary tree is only allowed once
        2.  for this function only, assume that the valued being searched (x) for is in the binary tree
        3.  n = 2^k - 1, because it is a full binary tree (of k levels)
"""
def avgBasicOpsFullTree(n):
    level = 1+(math.log(n)//math.log(2))
    level = int(level)
    total = 0
    for i in range(level):
        nodes = 2 ** (i)
        total += (nodes * ((i+1)/n))

    return total

def main():
    print(avgBasicOpsFullTree(7))


if __name__ == "__main__":
    main()
