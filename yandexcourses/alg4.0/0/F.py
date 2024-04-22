k = int(input())
n = int(input())

a = [int(input()) for i in range(n)]
t = 0
for i in range(n)[::-1]:
    t += a[i] // k * (i + 1) * 2
    a[i] %= k

i = n - 1

while i >= 0:
    temp = 0
    free = k
    if a[i] > 0:
        t += 2 * (i + 1)
        temp += a[i]
        free -= a[i]
        a[i] = 0
        for j in range(i):
            if a[i - j - 1] > 0 and free > 0:
                if a[i - j - 1] > free:
                    temp = k
                    a[i - j - 1] -= free
                    free = 0
                    i = i - j - 1
                    break
                else:
                    temp += a[i - j - 1]
                    a[i - j - 1] = 0
                    free = k - temp
    
    else:
        i -= 1
                


print(t)