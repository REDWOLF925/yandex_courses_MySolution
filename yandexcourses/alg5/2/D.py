n = int(input())
board = [[0 for j in range(10)] for i in range(10)]

for i in range(n):
    x, y = map(int, input().split())
    board[y][x] = 1

ans = 0

for i in range(1, 9):
    for j in range(1, 9):
        if board[i][j] == 1:
            ans += 4 - board[i][j - 1] - board[i][j + 1] - board[i - 1][j] - board[i + 1][j]

print(ans)