n = int(input())
ships = []

for i in range(n):
    x, y = map(int, input().split())
    ships.append([x, y])

dists = [0 for i in range(n)]
pos = [{j:0 for j in range(1, n + 1)} for i in range(1, n + 1)]

for i in range(n): 
    for j in range(n):
        if j != i:
            dists[i] += abs(ships[i][1] - ships[j][1])
            pos[i][ships[j][0]] += 1

for i in range(n):
    for j in range(1, ships[i][0]):
        for k in range(1, n + 1):
            if pos[i][k] > 0:
                dists[i] += abs(j - k)
                pos[i][k] -= 1
                break

    for j in range(n, ships[i][0], -1):
        for k in range(n, 0, -1):
            if pos[i][k] > 0:
                dists[i] += abs(j - k)
                pos[i][k] -= 1
                break
        
print(min(dists))
