import math
x1, y1, x2, y2 = map(int, input().split())

r1 = (x1**2 + y1**2)**(1 / 2)
r2 = (x2**2 + y2**2)**(1 / 2)
straight = r1 + r2

angle1 = math.atan2(x1, y1) * 180 / math.pi
angle2 = math.atan2(x2, y2) * 180 / math.pi
angle = min(abs(angle1 - angle2), 360 - abs(angle1 - angle2))
radial = 2 * math.pi * min(r1, r2) * angle / 360 + abs(r1 - r2)

print(min(straight, radial))