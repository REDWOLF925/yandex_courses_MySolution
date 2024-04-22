a = int(input())
b = int(input())
n = int(input())

b = (b + n - 1) // n

if a > b:
    print('Yes')
else:
    print('No')