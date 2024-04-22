n, k = map(int, input().split())
seq = list(map(int, input().split()))

ans = 0

for i in range(n - 1):
    for j in range(1, min(n - i, k + 1)):
        diff = seq[i + j] - seq[i]
        if diff > ans:
            ans = diff

print(ans)