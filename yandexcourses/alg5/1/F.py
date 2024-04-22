n = int(input())
seq = list(map(int, input().split()))
s = ''
L = 0
R = 1
while R < n and (seq[L] % 2 != 1 or seq[R] % 2 != 0):
    if seq[L] % 2 != 1:
        L += 1
        R += 1
    elif seq[R] % 2 != 0:
        R += 1

for i in range(1, n):
    if i <= L:
        print('+', end='')
    elif i < R:
        print('x', end='')
    elif i == R:
        print('+', end='')
    elif i > R:
        print('x', end='')
