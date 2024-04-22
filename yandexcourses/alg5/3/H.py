n = int(input())

a = set()
for i in range(n):
    xy = tuple(map(int, input().split()))
    a.add(xy)

b = set()
for i in range(n):
    xy = tuple(map(int, input().split()))
    b.add(xy)

d = dict()
maxcnt = 0

for el1 in a:
    for el2 in b:
        dxy1 = [el2[0] - el1[0], 
               el2[1] - el1[1], 
               el2[2] - el1[2], 
               el2[3] - el1[3]
               ]
        dxy2 = [el2[0] - el1[2], 
               el2[1] - el1[3], 
               el2[2] - el1[0], 
               el2[3] - el1[1]
               ]
        if dxy1[0] == dxy1[2] and dxy1[1] == dxy1[3]:
            pair = (dxy1[0], dxy1[1])
            if pair not in d:
                d[pair] = 0
            d[pair] += 1
            if d[pair] > maxcnt:
                maxcnt = d[pair]
        elif dxy2[0] == dxy2[2] and dxy2[1] == dxy2[3]:
            pair = (dxy2[0], dxy2[1])
            if pair not in d:
                d[pair] = 0
            d[pair] += 1
            if d[pair] > maxcnt:
                maxcnt = d[pair]

print(n - maxcnt)