dict1 = {} 
dict2 = {}
str1 = input()
str2 = input()

for char in str1:
    if char in dict1:
        dict1[char] += 1
    else: 
        dict1[char] = 1

for char in str2:
    if char in dict2:
        dict2[char] += 1
    else: 
        dict2[char] = 1


if set(dict1.keys()) == set(dict2.keys()) and set(dict1.values()) == set(dict2.values()):
    print('YES')
else:
    print('NO')