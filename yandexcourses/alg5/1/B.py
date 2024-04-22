g11, g12 = map(int, input().split(':'))
g21, g22 = map(int, input().split(':'))
ind = int(input())

if ind == 1:
    go1 = g21
    go2 = g12
else:
    go1 = g11
    go2 = g22

if g11 + g21 > g12 + g22:
    print(0)
elif g11 + g21 == g12 + g22:
    if go1 > go2:
        print(0)
    else:
        print(1)
else:
    ans = g12 + g22 - (g11 + g21)
    if ind == 1 and go1 + ans > go2:
        print(ans)
    elif ind == 2 and go1 > go2:
        print(ans)
    else:
        print(ans + 1)
