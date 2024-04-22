s1 = input()
s2 = input()
d1 = dict()
d2 = dict()

for i in s1:
    if i not in d1:
        d1[i] = 0
    d1[i] += 1

for i in s2:
    if i not in d2:
        d2[i] = 0
    d2[i] += 1

if d1 == d2:
    print('YES')
else:
    print('NO')