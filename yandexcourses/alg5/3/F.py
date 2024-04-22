d = set(input().split())
maxld = 0

for w in d:
    if len(w) > maxld:
        maxld = len(w)

s = list(input().split())

for w in s:
    flag = False
    for i in range(maxld):
        if w[:i + 1] in d:
            print(w[:i + 1], end=' ')
            flag = True
            break
    if not flag:
        print(w, end=' ')
