n, s, f = map(int, input().split())
a = [[0 for i in range(n + 1)] for j in range(n + 1)]
heap = {}

for i in range(1, n + 1):
    b = list(map(int, input().split()))
    a[i][1:] = b
    if i != s:
        heap[i] = 10**5

if s == f:
    print(0)
else:
    
    visited = [False for i in range(n + 1)]
    dist = [10**5 for i in range(n + 1)]
    visited[s], dist[s] = (True, 0)
    t = s

    while heap:
        visited[t] = True
        for i in range(1, n + 1):
            if a[t][i] >= 0 and i != t:
                if not visited[i] and dist[t] + a[t][i] < dist[i]:
                    dist[i] = dist[t] + a[t][i]
                    heap[i] = dist[i]
        if t == f:
            break
        t = min(heap, key=heap.get)
        heap.pop(t)

    if dist[f] >= 10**5:
        print(-1)
    else:
        print(dist[f])
