def isequal(l, a, b):
    b = n - b + 1
    temp1 = (h[a - 1 + l] + hm[b - 1] * x[l]) % p
    temp2 = (hm[b - 1 + l] + h[a - 1] * x[l]) % p
    return temp1 == temp2

def ispol(curr):
    k = 0
    maxl = min(curr - 1, n - curr)
    minl = 0
    if maxl >= 1:
        if not isequal(maxl, curr - maxl, curr + maxl):
            while maxl >= 1 and minl < maxl:
                currl = (maxl - minl) // 2 + 1 + minl
                if isequal(currl, curr - currl, curr + currl):
                    minl = currl
                else:
                    maxl = currl - 1
            
        k = maxl
    maxl = min(curr, n - curr)
    minl = 0

    if not isequal(maxl, curr - maxl + 1, curr + maxl):
        while maxl >= 1 and minl < maxl:
            currl = (maxl - minl) // 2 + 1 + minl
            if isequal(currl, curr - currl + 1, curr + currl):
                minl = currl
            else:
                maxl = currl - 1
        k += maxl
    else:
        k += maxl
    
    return(k)

s = input()
if s:
    n = len(s)
    h = [0]
    hm = [0]
    x_ = 257
    p = 10**10 + 7
    s = ' ' + s
    x = [1]
    for i in range(1, n + 1):
        h.append((h[i - 1] * x_ + ord(s[i])) % p)
        hm.append((hm[i - 1] * x_ + ord(s[n - i + 1])) % p)
        x.append((x[i - 1] * x_) % p)

    pols = n

    for i in range(1, n):
        pols += ispol(i)

    print(pols)