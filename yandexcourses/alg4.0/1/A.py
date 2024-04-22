def partition(n, a, x):
    
    E = 0
    G = 0
    for N in range(n):
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
    return E

n = int(input())
a = [int(i) for i in input().split()]
x = int(input())

E = partition(n, a, x)
print(E)
print(n - E)