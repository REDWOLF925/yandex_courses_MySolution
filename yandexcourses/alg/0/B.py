def hcf(a,b): 
    while b:
        (a, b) = (b, a % b) 
    return a 

a, b, c, d = map(int, input().split())

ch = a * d + c * b
zn = b * d

temp = hcf(ch, zn)

print(ch//temp, zn//temp)