t = int(input())

for i in range(t):
    n, a, b = map(int, input().split())
    groups = n // a
    reminder = n % a
    if (b - a) * groups >= reminder:
        print('YES')
    else:
        print('NO')