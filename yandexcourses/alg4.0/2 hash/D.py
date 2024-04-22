def isequal(l, b):
    a = 1
    temp1 = (h[a - 1 + l] + hm[b - 1] * x[l]) % p
    temp2 = (hm[b - 1 + l] + h[a - 1] * x[l]) % p
    return temp1 == temp2

n, m = map(int, input().split())
s = list(map(int, input().split()))
n = len(s)
h = [0]
hm = [0]
x_ = m + 1
p = 10**9 + 7
x = [1]
z = [0]*n
for i in range(0, n):
    h.append((h[i] * x_ + s[i]) % p)
    hm.append((hm[i] * x_ + s[n - i - 1]) % p)
    x.append((x[i] * x_) % p)

t = []
if n % 2 != 0:
    n_ = n // 2 + 1
else:
    n_ = n // 2
for i in range(n_, n):
    if isequal(n - i, 2 * i - n + 1):
        t.append(i)
t.append(n)

for i in t:
    print(i, end=' ')
