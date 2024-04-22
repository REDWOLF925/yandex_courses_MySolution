a = [['*' for i in range(8)] for j in range(8)]

for i in range(8):
    s = input()
    for j in range(8):
        if s[j] == 'R':
            a[i][j] = 'R'
        if s[j] == 'B':
            a[i][j] = 'B'

ans = 0

for i in range(8):
    for j in range(8):
        if a[i][j] == 'R':
            k = 1
            while i - k >= 0 and (a[i - k][j] != 'R' and a[i - k][j] != 'B'):
                a[i - k][j] = '-'
                k += 1
            k = 1
            while i + k <= 7 and (a[i + k][j] != 'R' and a[i + k][j] != 'B'):
                a[i + k][j] = '-'
                k += 1
            k = 1
            while j - k >= 0 and (a[i][j - k] != 'R' and a[i][j - k] != 'B'):
                a[i][j - k] = '-'
                k += 1
            k = 1
            while j + k <= 7 and (a[i][j + k] != 'R' and a[i][j + k] != 'B'):
                a[i][j + k] = '-'
                k += 1
        
        if a[i][j] == 'B':
            k = 1
            while min(i, j) - k >= 0 and (a[i - k][j - k] != 'R' and a[i - k][j - k] != 'B'):
                a[i - k][j - k] = '-'
                k += 1
            k = 1
            while max(i, j) + k <= 7 and (a[i + k][j + k] != 'R' and a[i + k][j + k] != 'B'):
                a[i + k][j + k] = '-'
                k += 1
            k = 1
            while j - k >= 0 and i + k <= 7 and (a[i + k][j - k] != 'R' and a[i + k][j - k] != 'B'):
                a[i + k][j - k] = '-'
                k += 1
            k = 1
            while j + k <= 7 and i - k >= 0 and (a[i - k][j + k] != 'R' and a[i - k][j + k] != 'B'):
                a[i - k][j + k] = '-'
                k += 1
        
for i in range(8):
    for j in range(8):
        if a[i][j] == '*':
            ans += 1

print(ans)