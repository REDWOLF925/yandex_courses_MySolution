def bitwisesort(a):
    for i in range(m):
        b = [[] for i in range(10)]
        print('**********')
        print('Phase', i + 1)
        for j in range(n):
            b[int(a[j][m - 1 - i])].append(a[j])
        k = 0
        for j in range(10):
            s = ', '.join(ch for ch in b[j])
            if b[j]:
                for ch in b[j]:
                    a[k] = ch
                    k += 1
            if not b[j]:
                s = 'empty'
            print(f'Bucket {j}: {s}')
    print('**********')


n = int(input())
a = []
if n > 0:
    for i in range(n):
        a.append(input())
    m = len(str(max(a)))

    print('Initial array:')
    print(', '.join(ch for ch in a))

    bitwisesort(a)

    print('Sorted array:')
    print(', '.join(ch for ch in a))
