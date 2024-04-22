def rec(n, used, prefix=[]):
    if len(prefix) == n:
        print(''.join(prefix))
        return
  
    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            prefix.append(str(i))
            rec(n, used, prefix)
            used[i] = False
            prefix.pop()

n = int(input())
used = [False for i in range(n + 1)]

rec(n, used)