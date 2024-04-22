n = int(input())
raiting = list(map(int, input().split()))

score = [0 for i in range(n)]
sum_score = 0
for i in range(1, n):
    sum_score += raiting[i - 1]
    score[i] = i * raiting[i] - sum_score

sum_score = 0
for i in range(1, n):
    sum_score += raiting[n - i]
    score[n - i - 1] += sum_score - i * raiting[n - i - 1]

for i in range(n):
    print(score[i], end=' ')
