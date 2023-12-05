n, m = map(int, input().split())
a = [int(i) for i in input().split()]

for i in range(m):
    l, r = map(int, input().split())
    b = a[l:r + 1]
    key = min(b)
    if b.count(key) == r - l + 1:
        print('NOT FOUND')
    else:
        for i in b:
            if i != key:
                print(i)
                break