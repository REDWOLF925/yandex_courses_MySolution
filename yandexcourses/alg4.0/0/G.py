n, m = map(int, input().split())

ll = []

for i in range(n):
    l = list(map(int, input().split()))
    ll.append(l)

a = [[0 for j in range(m)] for i in range(n)]

maxs = 0

for i in range(max(n, m)):
    if i < n and ll[i][0] == 1:
        a[i][0] = 1
        maxs = 1
    if i < m and ll[0][i] == 1:
        a[0][i] = 1
        maxs = 1

for i in range(1, n):
    for j in range(1, m):
        if ll[i][j] == 1:
            a[i][j] = min(a[i - 1][j - 1], a[i][j - 1], a[i - 1][j]) + 1
            if a[i][j] > maxs:
                maxs = a[i][j]

print(maxs)