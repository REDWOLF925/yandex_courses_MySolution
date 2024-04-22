n, m = map(int, input().split())
maxi1 = [0 for i in range(n)]
maxj1 = [0 for j in range(m)]

maxi2 = [0 for i in range(n)]
maxj2 = [0 for j in range(m)]
a = [[] for i in range(n)]

maxjel1 = 0
maxiel1 = 0

maxjel2 = 0
maxiel2 = 0

for i in range(n):
    a[i] = list(map(int, input().split()))
    maxi1[i] = max(a[i])
    if maxi1[i] > maxiel1:
        maxiel1 = maxi1[i]
        argmaxi1 = i
    for j in range(m):
        maxj2[j] = max(maxj2[j], a[i][j])
        if maxj2[j] > maxjel2:
            maxjel2 = maxj2[j]
            argmaxj2 = j

for i in range(n):
    for j in range(m):
        if i != argmaxi1:
            maxj1[j] = max(maxj1[j], a[i][j])
            if maxj1[j] > maxjel1:
                maxjel1 = maxj1[j]
                argmaxj1 = j
        if j != argmaxj2:
            maxi2[i] = max(maxi2[i], a[i][j])

    if maxi2[i] > maxiel2:
        maxiel2 = maxi2[i]
        argmaxi2 = i
    
maxel1 = 0
maxel2 = 0

for i in range(n):
    for j in range(m):
        if i != argmaxi1 and j != argmaxj1:
            if a[i][j] > maxel1:
                maxel1 =  a[i][j]
        if i != argmaxi2 and j != argmaxj2:
            if a[i][j] > maxel2:
                maxel2 =  a[i][j]

if maxel2 < maxel1:
    print(argmaxi2 + 1, argmaxj2 + 1)
else:
    print(argmaxi1 + 1, argmaxj1 + 1)