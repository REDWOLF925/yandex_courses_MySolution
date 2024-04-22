def check(seq, m, k):
    sum_ = 0
    for i in range(m, m + k):
        sum_ += seq[i]
    return sum_

def binsearch(psum, k, s):
    l = 0
    r = len(psum) - 1 - k
    while l <= r:
        m = (l + r) // 2
        t = psum[m] - psum[m + k]
        if t < s:
            l = m + 1
        elif t > s:
            r = m - 1
        else:
            return m
    
    return -2

n, m = map(int, input().split())
seq = list(map(int, input().split()))
sum_ = sum(seq)
psum = [0 for i in range(n + 1)]
psum[0] = sum_
for i in range(1, n + 1):
    psum[i] = psum[i - 1] - seq[i - 1]
for i in range(m):
    l, s = map(int, input().split())
    print(binsearch(psum, l, s) + 1)