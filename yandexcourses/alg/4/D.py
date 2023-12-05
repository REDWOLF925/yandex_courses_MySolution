import heapq

def rec(n, used, length, pos=1, summ=0):
    if summ >= length:
        return length
    elif False not in used:
        if a[pos][1] > 0 and a[pos][1] + summ < length:
            return a[pos][1] + summ
        else:
            return length

    for i in range(1, n + 1):
        if not used[i] and a[pos][i] > 0:
            used[i] = True
            length = rec(n, used, length, i, summ + a[pos][i])
            used[i] = False

    return length


n = int(input())
a = [[-1 for i in range(n + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    b = list(map(int, input().split()))
    a[i][1:] = b

s = 1

if n == 1:
    print(0)
elif n > 1:
    heap = [(0, str(s))]
    
    visited = [False for i in range(n + 1)]
    dist = [-1 for i in range(n + 1)]
    dist[s] = 0
    t = s

    while heap:
        temp = heapq.heappop(heap)
        t = int(temp[1])
        if visited[t]:
            continue
        visited[t] = True
        dist[t] = temp[0]
        heap = []
        for i in range(1, n + 1):
            if i != t and a[t][i] > 0:
                heapq.heappush(heap, (dist[t] + a[t][i], str(i)))

    if False not in visited[1:] and a[dist.index(max(dist))][1] > 0:
        dxtr = max(dist) + a[dist.index(max(dist))][1]
    else:
        dxtr = 10**(10)

    used = [False for i in range(n + 1)]
    used[1] = True
    used[0] = True

    comm = rec(n, used, dxtr)
    if comm != 10**(10):
        print(comm)
    else:
        print(-1)
