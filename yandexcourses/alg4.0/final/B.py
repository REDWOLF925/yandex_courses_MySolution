def isequal(l, a, b):
    b = n - b + 1
    temp1 = (h[a - 1 + l] + hm[b - 1] * x[l]) % p
    temp2 = (hm[b - 1 + l] + h[a - 1] * x[l]) % p
    return temp1 == temp2

def z_func(i, n):
    m = 0
    n_ = i
    temp = 0
    while n_ >= 1 and m < n_:
        k = (m + n_) // 2 + 1
        if isequal(k, 1, i):
            m = k
            if k > temp:
                temp = k
        else:
            n_ = k - 1

    return n_

n = int(input())
s = input()
h = [0]
hm = [0]
x_ = 257
p = 10**9 + 7
s = ' ' + s
x = [1]
z = [0]*n
for i in range(1, n + 1):
    h.append((h[i - 1] * x_ + ord(s[i])) % p)
    hm.append((hm[i - 1] * x_ + ord(s[n - i + 1])) % p)
    x.append((x[i - 1] * x_) % p)

print(1, end=' ')

for i in range(2, n + 1):
    n_ = n - i + 1
    print(z_func(i, n_), end=' ')