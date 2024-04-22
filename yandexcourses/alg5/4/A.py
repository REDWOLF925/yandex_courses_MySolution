def lbinsearch(seq, k):
    l = 0
    r = len(seq) - 1
    while l < r:
        m = (l + r) // 2
        if seq[m] < k:
            l = m + 1
        else:
            r = m
    
    return l

def rbinsearch(seq, k):
    l = 0
    r = len(seq) - 1
    while l < r:
        m = (l + r + 1) // 2
        if seq[m] > k:
            r = m - 1
        else:
            l = m
    
    return r

n = int(input())
seq = list(map(int, input().split()))
seq.sort()
k = int(input())
if n > 1:
    for i in range(k):
        a, b = map(int, input().split())
        r = rbinsearch(seq, b) 
        l = lbinsearch(seq, a)
        if seq[r] < a or seq[l] > b:
            print(0, end=' ')
        else:
            print(r - l + 1, end=' ')
else:
    for i in range(k):
        a, b = map(int, input().split())
        if seq[0] >= a and seq[0] <= b:
            print(1, end=' ')
        else:
            print(0, end=' ')
