# I declare that the following source code was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.
# I declare that the following source code was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

"""
    Please implement functions named:  reset, basicOps, quickSort, partition, bestBasicOps, and worstBasicOps; details follow.

    You don't have to, but you might want to, add a main function and code/test this in your
    favorite Python IDE.

"""

""" reset, resets basic op counter to 0 """
import math
import time
import random
numOps = 0
sumoftimes = 0
sumoflogitems = 0

def reset():
    global numOps
    numOps = 0


""" basicOps returns the number of basic operations """
def basicOps():
    global numOps
    return numOps


""" 
    quickSort, implement quickSort
"""
def quickSort(listToSort, low, high):
    global numOps
    #   parameter a is a list of items to sort in non-decreasing order
    #   low = index into a for beginning of which keys to sort
    #   high = index into a for end of which keys to sort
    #
    #   quickSort algorithm:
    #       terminal condition is when low >= high
    #
    #       otherwise:
    #           pivotPoint = partition(listToSort, low, high pivotPoint)
    #           quickSort(listToSort, low, pivotPoint)
    #           quickSort(listToSort, pivotPoint + 1, high)
    if low<high:
       partitionIndex = partition(listToSort, low, high) 
       
       quickSort(listToSort, low, partitionIndex - 1)
       
       quickSort(listToSort, partitionIndex + 1, high)


""" 
    partition, partitions a[low..high] about pivot (the first element)
    returns partitionIndex (where the line in the sand between lower key <= pivotItem <= highest key
"""
def partition(a, low, high):
    global numOps
    numOps += high - low
    #   parameter a is a list of items of size n, that will be partitioned into
    #   either higher or lower than the pivot
    #
    #   partition:
    #       pivotItem is the item used for key comparisons (a[low])
    #       index of is the index into a, of a next item for key comparisons
    #         (don't forget the +1 for not comparing pivotItem to itself)
    #       pivotIndex is the index into a, of where to swap next item into and out of
    #         to move items less than partition into left side of array (less than pivot)
    #
    #       while (indexOfKey < high)
    #           if (a[indexOfKey] < pivotItem) then
    #               exchange a[indexOfKey] and a[pivotIndex]
    #               // don't want to stomp previous data when moving next item less than pivot
    #               // also, don't want to have pivot index be 0, if there's something below it
    #               // so doing
    #               pivotIndex++
    #           indexOfKey++ // now let's do the same thing for the next key/item
    #
    #
    #  move pivotItem into pivot index, if it isn't already the lowest item
    pivot = a[low]
    start = low + 1
    end = high
    
    while True:
        while start <= end and a[end] >= pivot:
            end = end - 1
            
            
        while start <= end and a[start] <= pivot:
            start = start + 1
            
        if start <= end:
            a[start], a[end] = a[end], a[start]
            
            
        else:
            break
        
    a[low], a[end] = a[end], a[low]
    
    
    return end
    


""" 
    bestBasicOps, for a list the size of n, where n is a power of 2 (n = 2^k), this function 
    returns b(n), aka the best case or minimal number of key comparisons, as a double

    best case of quick sort only does n - 1 key comparisons but splits the items equally around pivot

    therefore, for bestBasicOps, assume that the recurrence relation is:
        b(1) = 0
        b(n) = 2*b(n/2) + n - 1 

    Hint: starting with given b(1), calculate b(2), b(4), etc. until you find a pattern.
    Using the pattern, find a closed form solution.  Then use induction to prove it's true.
    Finally implement here the correct, proven, best-case candidate (closed form) solution.
"""
def bestBasicOps(n):
    # best quickSort == worst mergeSort
    myAns = (math.log2(n)-1) * n + 1
    return myAns


""" 
    worstBasicOps, for a list the size of n, where n is a power of 2 (n = 2^k), this function 
    returns w(n), aka the worst case or maximum number of key comparisons, as a double

    worst case of quick sort does n-1 key comparisons because there's no need to compare the last element to itself

    therefore, for worstBasicOps, assume that the recurrence relation is:
        w(1) = 0
        w(n) = w(n-1) + n - 1 

    Hint: starting with given w(1), calculate w(2), w(4), etc. until you find a pattern.
    from this pattern, find a closed form solution.  Then use induction to prove it's true.
    Finally, implement here the correct, proven, worst-case candidate (closed form) solution.

"""
def worstBasicOps(n):
   myAns = (n*(n-1))/2
   return myAns

def main():
    reset()
    global sumoftimes
    global sumoflogitems
    myList = [2**10, 2**15, 2**20, 2**25]
    for x in myList:
        randomlist = random.sample(range(1,1500000000), x)
        initial = time.perf_counter()
        quickSort(randomlist, 0, x-1)
        final = time.perf_counter()
        timer = final-initial
        sumoftimes += timer
        sumoflogitems += x*math.log2(x)
        c = sumoftimes / sumoflogitems
        numbasicops = basicOps()
        estimatedtime = c * numbasicops
        print("Basic operations: " + str(numbasicops))
        print("Estimated time: " + str(estimatedtime) + " seconds")
        print("Total time is " + str(timer) + " seconds")

    
    
if __name__ == "__main__":
    main()