n = int(input())
ans = 0

for i in range(n):
    ai = int(input())
    ans += ai // 4
    if ai % 4 == 3:
        ans += 2
    else:
        ans += ai % 4

print(ans)