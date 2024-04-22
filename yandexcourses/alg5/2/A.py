n = int(input())
x, y = map(int, input().split())

minx = maxx = x
miny = maxy = y

for i in range(1, n):
    x, y = map(int, input().split())
    if x < minx:
        minx = x
    if x > maxx:
        maxx = x
    if y < miny:
        miny = y
    if y > maxy:
        maxy = y

print(minx, miny, maxx, maxy)