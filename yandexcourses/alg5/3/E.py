n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))
n3 = int(input())
s3 = set(map(int, input().split()))

ans = (s1 & s2) | (s2 & s3) | (s3 & s1)

if len(ans) == 0:
    print()
for i in sorted(ans):
    print(i, end=' ')