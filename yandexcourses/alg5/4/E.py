def diagn(n):
    l = 0
    r = n
    while l < r:
        m = (l + r + 1) // 2
        if (m + 1) * m // 2 >= n:
            r = m - 1
        else:
            l = m
    return r

n = int(input())
k = diagn(n)
d = n - (k + 1) * k // 2

if k % 2 == 0:
    print(d, '/', k + 2 - d, sep='')
else:
    print(k + 2 - d, '/', d, sep='')