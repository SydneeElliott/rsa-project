
numOps = 0
""" reset, resets basic op counter to 0 """
def reset():
    global numOps
    numOps = 0

def basicOps():
    global numOps
    return numOps

def geneSeqDP(s1, s2):
    m = len(s1)
    n = len(s2)
    
    # penalties
    indel = 5
    match = -3
    subst = 1
    
    global numOps
    numOps = 3 * m * n

    s = [[0] * (n + 1) for i in range(m + 1)]

    # rows
    for i in range(1, m+1):
        s[i][0] = i*indel
    
    # columns
    for j in range(1, n+1):
        s[0][j] = j*indel

    # best alignment
    for i in range(1, m+1):
        for j in range(1, n+1):
            dist = match if s1[i-1] == s2[j-1] else subst
            s[i][j] = min(s[i-1][j-1] + dist, s[i-1][j] + indel, s[i][j-1] + indel)

    return s[m][n]
  
def timeComplexity(m, n):
    mynum = m*n + m + n
    return mynum

def spaceComplexity(m, n):
    mynum = (m+1) * (n+1)
    return mynum

def main():
    reset()
    global sumoftimes
    myList = [2**10, 2**15, 2**20, 2**25]
    for x in myList:
        randomM = random.sample(range(1,1500000000), x)
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