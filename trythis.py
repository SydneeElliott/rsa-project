counter = 0
s1 = ""
s2 = ""
memoizationCache = {}

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
    counter += 1
    
    if i < 0:
        result = (j+1) * 5
        memoizationCache[(i,j)] = result
        return result

    elif j < 0:
        result = (i+1) * 5
        memoizationCache[(i,j)] = result
        return result
        
    if (i,j) in memoizationCache:
        return memoizationCache[(i,j)]
    
    match = genSeqDC(i-1, j-1) + (-3 if s1[i] == s2[j] else 1)
    memoizationCache[(i-1,j-1)] = match
    delete = genSeqDC(i-1, j) + 5
    memoizationCache[(i-1,j)] = delete
    insert = genSeqDC(i, j-1) + 5
    memoizationCache[(i,j-1)] = insert
    
    result = min(match, delete, insert)
    memoizationCache[(i,j)] = result
    return result

def main():
    global s1
    global s2
    s1 = 'TTGCTT'
    s2 = 'ATCGCCA'

    memoGenSeqDC(5, 6)
    print(memoizationCache)

if __name__ == '__main__':
    main()