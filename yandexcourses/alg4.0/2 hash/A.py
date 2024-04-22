s = input()
n = len(s)
h = [0]
x_ = 257
p = 10**9 + 7
s = ' ' + s
x = [1]
for i in range(1, n + 1):
    h.append((h[i - 1] * x_ + ord(s[i])) % p)
    x.append((x[i - 1] * x_) % p)

q = int(input())

for k in range(q):
    l, a, b = map(int, input().split())
    temp1 = (h[a + l] + h[b] * x[l]) % p
    temp2 = (h[b + l] + h[a] * x[l]) % p
    if temp1 == temp2:
        print('yes')
    else:
        print('no')