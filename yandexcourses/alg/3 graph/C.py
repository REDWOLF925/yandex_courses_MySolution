import heapq

n, k = map(int, input().split())
a = [[] for j in range(n + 1)]
if k > 0:
    for i in range(k):
        b = list(map(int, input().split()))
        a[b[0]].append((b[1],b[2]))
        a[b[1]].append((b[0],b[2]))

s, f = map(int, input().split())

if s == f:
    print(0)
elif k == 0:
    print(-1)
else:
    heap = [(0, str(s))]
    
    visited = [False for i in range(n + 1)]
    dist = [-1 for i in range(n + 1)]
    dist[s] = 0
    t = s

    while t != f and heap:
        temp = heapq.heappop(heap)
        t = int(temp[1])
        if visited[t]:
            continue
        visited[t] = True
        dist[t] = temp[0]
        for i in a[t]:
            heapq.heappush(heap, (dist[t] + i[1], str(i[0])))

    if dist[f] == -1:
        print(-1)
    else:
        print(dist[f])
