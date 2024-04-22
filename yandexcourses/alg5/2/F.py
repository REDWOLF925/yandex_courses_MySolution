n = int(input())
seq = list(map(int, input().split()))
a, b, k = map(int, input().split())

rightmin = (a - 1) // k % n
rightmax = (b - 1) // k % n

leftmin = (n - (a - 1) // k) % n
leftmax = (n - (b - 1) // k) % n

ans = seq[rightmin]

if - (a - 1) // k + (b - 1) // k >= n:
    for i in range(n):
        if seq[i] > ans:
            ans = seq[i]
else:
    if rightmin < rightmax:
        for i in range(rightmin, rightmax + 1):
            if seq[i] > ans:
                ans = seq[i]
    elif (a - 1) // k < (b - 1) // k:
        for i in range(rightmin, n):
            if seq[i] > ans:
                ans = seq[i]
        for i in range(rightmax + 1):
            if seq[i] > ans:
                ans = seq[i]

    if leftmin > leftmax or (a - 1) // k == (b - 1) // k:
        for i in range(leftmax, leftmin + 1):
            if seq[i] > ans:
                ans = seq[i]
    elif (a - 1) // k < (b - 1) // k:
        for i in range(leftmin + 1):
            if seq[i] > ans:
                ans = seq[i]
        for i in range(leftmax, n):
            if seq[i] > ans:
                ans = seq[i]

print(ans)