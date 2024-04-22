def isequal(l, a, b):
    temp1 = (h[a - 1 + l] + h[b - 1] * x[l]) % p
    temp2 = (h[b - 1 + l] + h[a - 1] * x[l]) % p
    return temp1 == temp2

s = input()
if s:
    n = len(s)
    h = [0]
    x_ = 257
    p = 10**9 + 7
    s = ' ' + s
    x = [1]
    for i in range(1, n + 1):
        h.append((h[i - 1] * x_ + ord(s[i])) % p)
        x.append((x[i - 1] * x_) % p)

    for k in range(1, n + 1):
        if k == n or isequal(n - k, 1, k + 1):
            print(k)
            break