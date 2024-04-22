import random

def partition(l, r, x):
    E = l
    G = l
    for N in range(l, r):
        if a[N] < x:
            y = a[N]
            a[N] = a[G]
            a[G] = a[E]
            a[E] = y
            G += 1
            E += 1
        elif a[N] == x:
            y = a[N]
            a[N] = a[G]
            a[G] = y
            G += 1
    return [E, G]

def quicksort(l, r):
    if r - l <= 1:
        return
    x = a[random.randint(l, r - 1)]
    p = partition(l, r, x)
    quicksort(l, p[0])
    quicksort(p[1], r)
    
n = int(input())
if n > 0:
    a = [int(i) for i in input().split()]
    E = quicksort(0, n)
    s = ' '.join(str(c) for c in a)
    print(s)
else:
    print('')