n, k = map(int, input().split())
seq = list(map(int, input().split()))
d = dict()
flag = False

for i in range(n):
    if seq[i] in d and i - d[seq[i]] <= k:
        flag = True
        break
    d[seq[i]] = i

if flag:
    print('YES')
else:
    print('NO')