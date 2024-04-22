def check(n):
    sum_ = (n + 1) * n // 2 - 1
    for i in range(1, (n + 1) // 2 + 1):
        sum_ += 2 * i * (n + 1 - i)
    if n % 2 == 1:
        sum_ -= (n + 1) // 2 * (n + 1 - (n + 1) // 2)
    return sum_

def rbinsearch(n):
    l = 0
    r = min(n, 2000000)
    while l < r:
        m = (l + r + 1) // 2
        if check(m) > n:
            r = m - 1
        else:
            l = m
    
    return r

n = int(input())

print(rbinsearch(n))