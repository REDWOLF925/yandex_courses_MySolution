def merge(a, b):
    c = []
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    for k in range(n + m):
        if i == n:
            c.append(b[j])
            j += 1
        elif j == m:
            c.append(a[i])
            i += 1
        elif a[i] > b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    return c 

def mergesort(l, r):
    x = l + (r - l)//2
    if r - l > 2:
        mergesort(l, x)
        mergesort(x, r)
    if r - l > 1:
        a[l:r] = merge(a[l:x], a[x:r])


n = int(input())
if n > 0:
    a = [int(i) for i in input().split()]
    mergesort(0, n)
    print(' '.join(str(ch) for ch in a))
