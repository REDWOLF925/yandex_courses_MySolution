x = int(input())

A = 1
B = 1

for i in range(x):
    al = A**2
    bl = B**3
    if al == bl:
        A += 1
        B += 1
    if al > bl:
        B += 1
    if al < bl:
        A += 1

print(min(al, bl))