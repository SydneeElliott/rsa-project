import random
import time

s1 = ""
s2 = ""
memoizationCache = {}
DPtime = 0
MemoTime = 0
dpBasicOps = 0
memoBasicOps = 0

def geneSeqDP(s1, s2):
    m = len(s1)
    n = len(s2)

    global dpBasicOps
    dpBasicOps = 3 * m * n
    
    # penalties
    indel = 5
    match = -3
    subst = 1

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

def setS1(seq):
    global s1
    s1 = seq

def setS2(seq):
    global s2
    s2 = seq

def memoGenSeqDC(i, j):
    global s1
    global s2
    global memoBasicOps
    global memoizationCache
    
    if (i,j) in memoizationCache:
        return memoizationCache[(i,j)]

    memoBasicOps += 1
    
    if i < 0:
        result = (j+1) * 5
        memoizationCache[(i,j)] = result
        return result
    elif j < 0:
        result = (i+1) * 5
        memoizationCache[(i,j)] = result
        return result
    
    match = memoGenSeqDC(i-1, j-1) + (-3 if s1[i] == s2[j] else 1)
    delete = memoGenSeqDC(i-1, j) + 5
    insert = memoGenSeqDC(i, j-1) + 5
    
    result = min(match, delete, insert)
    memoizationCache[(i,j)] = result
    return result

def generateRandomSequence(length):
    return ''.join(random.choice(['A', 'C', 'G', 'T']) for _ in range(length))

def main():
    global DPtime
    global MemoTime
    global dpBasicOps
    global memoBasicOps

    myList = [2**1, 2**3, 2**5, 2**7]

    for i in myList:
        m = i
        n = i

        s1 = generateRandomSequence(m)
        s2 = generateRandomSequence(n)

        setS1(s1)
        setS2(s2)
        initialDP = time.perf_counter()
        geneSeqDP(s1, s2)
        finalDP = time.perf_counter()
        DPtimer = finalDP - initialDP
        DPtime += DPtimer

        initialMemo = time.perf_counter()
        memoGenSeqDC(m-1,n-1)
        finalMemo = time.perf_counter()

        Memotimer = finalMemo - initialMemo
        MemoTime += Memotimer

        DPestimatedOps = 3*m*n
        MemoEstimatedOps = m * (n+1)

        CDP = DPtime / DPestimatedOps
        CMemo = MemoTime / MemoEstimatedOps
        
        DPEstimatedTime = CDP * dpBasicOps
        MemoEstimatedTime = CMemo * memoBasicOps

        print("n = " + str(i))
        print("Average DP time: " + str(DPtime))
        print("Average Memo time: " + str(MemoTime) + "\n")

        print("Estimated DP time: " + str(DPEstimatedTime))
        print("Estimated Memo time: " + str(MemoEstimatedTime) + "\n")

        print("Average DP Basic Ops: " + str(dpBasicOps))
        print("Average Memo Basic Ops: " + str(memoBasicOps) + '\n')

        print("Estimated DP Basic Ops: " + str(DPestimatedOps))
        print("Estimated Memo Basic Ops: " + str(MemoEstimatedOps) + "\n")

        print("DP constant C: " + str(CDP))
        print("Memo constant C: " + str(CMemo) + "\n")


    return 1

if __name__ == "__main__":
    main()