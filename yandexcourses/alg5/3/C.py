n = int(input())
seq = list(map(int, input().split()))
d = dict()

for i in seq:
    if i not in d:
        d[i] = 0
    d[i] += 1

maxs = d[seq[0]]

for k in d:
    if d[k] > maxs:
        maxs = d[k]
    if k - 1 in d and d[k - 1] + d[k] > maxs:
        maxs = d[k - 1] + d[k]

print(len(seq) - maxs)