def isequal(l, a, b):
    temp1 = (h[a - 1 + l] + h[b - 1] * x[l]) % p
    temp2 = (h[b - 1 + l] + h[a - 1] * x[l]) % p
    return temp1 == temp2

def z_func(i, n):
    m = 0
    temp = 0
    while m <= n:
        k = (m + n) // 2
        if isequal(k, 1, i):
            m = k + 1
            if k > temp:
                temp = k
        else:
            n = k - 1

    return temp


s = input()
n = len(s)
h = [0]
x_ = 257
p = 10**9 + 7
s = ' ' + s
x = [1]
z = [0]*n
for i in range(1, n + 1):
    h.append((h[i - 1] * x_ + ord(s[i])) % p)
    x.append((x[i - 1] * x_) % p)

print(0, end=' ')

for i in range(2, n + 1):
    n_ = n - i + 1
    print(z_func(i, n_), end=' ')