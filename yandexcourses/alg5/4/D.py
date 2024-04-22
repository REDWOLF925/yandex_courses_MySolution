def linescnt(seq, w):
    ind = 0
    cnt = 0
    while ind < len(seq) - 1:
        l = 1
        r = len(seq) - ind - 1
        while l < r:
            m = (l + r + 1) // 2
            if seq[ind] - seq[ind + m] + m - 1 <= w:
                l = m
            else:
                r = m - 1
        ind += r
        cnt += 1
    return cnt

def binsearch(a, b, w, maxa, maxb):
    l = maxa
    r = w - maxb
    lcnt = linescnt(a, l)
    rcnt = linescnt(b, maxb)
    mprev = -1

    while l <= r:
        m = (l + r) // 2
        lcnt_ = linescnt(a, m)
        rcnt_ = linescnt(b, w - m)
        if max(lcnt_, rcnt_) > max(lcnt, rcnt):
            if m > mprev:
                l = mprev
                r = m - 1
            else:
                l = m + 1
                r = mprev
        if l == r:
            return min(max(lcnt, rcnt), max(lcnt_, rcnt_))
        
        if lcnt_ > rcnt_:
            l = m + 1
        elif lcnt_ < rcnt_:
            r = m - 1
        else:
            return lcnt_
        
        lcnt = lcnt_
        rcnt = rcnt_
        mprev = m
    
    return max(lcnt, rcnt)

w, n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
maxa = max(a)
maxb = max(b)
prea = [0 for i in range(n + 1)]
preb = [0 for i in range(m + 1)]
prea[0] = sum(a)
preb[0] = sum(b)

for i in range(1, n + 1):
    prea[i] = prea[i - 1] - a[i - 1]

for i in range(1, m + 1):
    preb[i] = preb[i - 1] - b[i - 1]

print(binsearch(prea, preb, w, maxa, maxb))