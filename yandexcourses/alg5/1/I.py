n = int(input())
year = int(input())
holidays = set()
for i in range(n):
    d, m = input().split()
    d = int(d)
    holidays.add((d, m))
dow = input()

if dow == 'Monday':
    ndow = 0
if dow == 'Tuesday':
    ndow = 1
if dow == 'Wednesday':
    ndow = 2
if dow == 'Thursday':
    ndow = 3
if dow == 'Friday':
    ndow = 4
if dow == 'Saturday':
    ndow = 5
if dow == 'Sunday':
    ndow = 6

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    k = 29
else:
    k = 28

dayscnt = [0 for i in range(7)]

def monthcnt(month, k, ndow):
    for i in range(k):
        if (i + 1, month) not in holidays:
            dayscnt[ndow] += 1
        ndow = (ndow + 1) % 7

months = [('January', 31),
          ('February', k),
          ('March', 31),
          ('April', 30),
          ('May', 31),
          ('June', 30),
          ('July', 31),
          ('August', 31),
          ('September', 30),
          ('October', 31),
          ('November', 30),
          ('December', 31)
          ]

for i in range(12):
    monthcnt(months[i][0], months[i][1], ndow)
    ndow = (ndow + months[i][1]) % 7

if dayscnt[1] > dayscnt[0]:
    dmin = dayscnt[0]
    dmax = dayscnt[1]
    wmin = 'Monday'
    wmax = 'Tuesday'
else:
    dmax = dayscnt[0]
    dmin = dayscnt[1]
    wmax = 'Monday'
    wmin = 'Tuesday'

dnames = {0:'Monday',
          1:'Tuesday',
          2:'Wednesday',
          3:'Thursday',
          4:'Friday',
          5:'Saturday',
          6:'Sunday'
          }

for i in range(2, 7):
    if dayscnt[i] > dmax:
        dmax = dayscnt[i]
        wmax = dnames[i]
    elif dayscnt[i] < dmin:
        dmin = dayscnt[i]
        wmin = dnames[i]

print(wmax, wmin)
