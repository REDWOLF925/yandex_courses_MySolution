n = int(input())
dots = set()
x, y = map(int, input().split())
dots.add((x, y))
dotsnew = set()
dotsnew.add((x, y))

k = 3
dotans = [(x + 1, y), (x, y - 1), (x + 1, y - 1)]

for i in range(1, n):
    x, y = map(int, input().split())
    dots.add((x, y))
    dotsnew.add((x, y))

for dot1 in dots:
    dotsnew.remove(dot1)
    for dot2 in dotsnew:
        lowdot1 = (dot1[0] + (dot2[1] - dot1[1]), dot1[1] - (dot2[0] - dot1[0]))
        lowdot2 = (dot2[0] + (dot2[1] - dot1[1]), dot2[1] - (dot2[0] - dot1[0]))
        uppdot1 = (dot1[0] - (dot2[1] - dot1[1]), dot1[1] + (dot2[0] - dot1[0]))
        uppdot2 = (dot2[0] - (dot2[1] - dot1[1]), dot2[1] + (dot2[0] - dot1[0]))
        if k > 2:
            k = 2
            dotans = [lowdot1, lowdot2]
            
        if lowdot1 in dots:
            if lowdot2 in dots:
                k = 0
                break
            elif k > 1:
                k = 1
                dotans = [lowdot2]
        elif lowdot2 in dots:
            if k > 1:
                k = 1
                dotans = [lowdot1]

        if uppdot1 in dots:
            if uppdot2 in dots:
                k = 0
                break
            elif k > 1:
                k = 1
                dotans = [uppdot2]
        elif uppdot2 in dots:
            if k > 1:
                k = 1
                dotans = [uppdot1]
    
    if k == 0:
        break

print(k)
for i in range(k):
    print(dotans[i][0], dotans[i][1])