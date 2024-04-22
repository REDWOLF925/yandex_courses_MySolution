def merge(n, m):
    c = []
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

n = int(input())
a = [int(i) for i in input().split()]

m = int(input())
b = [int(i) for i in input().split()]

if a or b:
    s = merge(n, m)
    print(' '.join(str(ch) for ch in s))