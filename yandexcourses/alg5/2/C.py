n = int(input())
seq = list(map(int, input().split()))

suml = seq[0]
maxl = seq[0]

for i in range(1, n):
    suml += seq[i]
    if seq[i] > maxl:
        maxl = seq[i]

if suml >= maxl * 2:
    print(suml)
else:
    print(2 * maxl - suml)