t = int(input())

for i in range(t):
    n = int(input())
    seq = list(map(int, input().split()))
    length = 1
    minel = seq[0]
    ans = []
    for i in range(1, n):
        if length >= minel or length >= seq[i]:
            ans.append(length)
            length = 0
            minel = seq[i]
        
        length += 1
        minel = min(minel, seq[i])
    
    ans.append(length)

    print(len(ans))
    print(' '.join(map(str, ans)))
