counter = 0
s1 = ""
s2 = ""
memoizationCache = {}

s1 = ""
s2 = ""

def reset():
    global counter
    global s1
    global s2
    counter = 0
    s1 = ""
    s2 = ""

def basicOps(): 
    global counter
    return counter
    
def setS1(seq):
    global s1
    s1 = seq

def setS2(seq):
    global s2
    s2 = seq

def genSeqDC(i, j):
    global s1
    global s2
    global counter
    counter += 1
    
    if i < 0:
        return (j+1) * 5
    elif j < 0:
        return (i+1) * 5
    
    match = genSeqDC(i-1, j-1) + (-3 if s1[i] == s2[j] else 1)
    delete = genSeqDC(i-1, j) + 5
    insert = genSeqDC(i, j-1) + 5
    
    return min(match, delete, insert)
    
def memoGenSeqDC(i, j):
    global s1
    global s2
    global counter
    global memoizationCache
    
    if (i,j) in memoizationCache:
        return memoizationCache[(i,j)]

    counter += 1
    
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