n = int(input())
k = int(input())
ans = set(input().split())

for i in range(1, n):
    k = int(input())
    ans &= set(input().split())

print(len(ans))
print(' '.join(sorted(ans)))