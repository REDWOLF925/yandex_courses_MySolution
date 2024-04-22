n, k, d = map(int, input().split())
flag = False

for i in range(10):
    ans = n * 10 + i
    if ans % k == 0:
        flag = True
        break
if flag:
    print(ans, end='')
    for i in range(d - 1):
        print(0, end='')
else:
    print(-1)