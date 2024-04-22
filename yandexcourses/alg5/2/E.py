n = int(input())

berries = []
posb = -1
bind = -1
nega = -1
aind = -1
ans = 0
neg = set()
pos = set()

for i in range(n):
    a, b = map(int, input().split())
    berries.append([a, b])
    diff = a - b
    if diff > 0:
        ans += diff
        pos.add(i + 1)
        if posb < b:
            posb = b
            bind = i + 1
    else:
        neg.add(i + 1)
        if nega < a:
            nega = a
            aind = i + 1

if nega > posb:
    ans += nega
    neg.remove(aind)
    key = str(aind)
else:
    ans += posb
    pos.remove(bind)
    key = str(bind)

print(ans)
print(' '.join(map(str, pos)), end=' ')
print(key, end=' ')
print(' '.join(map(str, neg)))