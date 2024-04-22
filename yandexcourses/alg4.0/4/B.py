def rec(n, count, col):
    if col == n:
        return count + 1

    for i in range(n):
        if not row[i]:
            if not diag2[i + col] and not diag1[n - 1 + i - col]:
                row[i] = True
                diag2[i + col] = True
                diag1[n - 1 + i - col] = True
                col += 1
                count = rec(n, count, col)
                col -= 1
                row[i] = False
                diag2[i + col] = False
                diag1[n - 1 + i - col] = False

    return(count)


n = int(input())
diag1 = [False for i in range(2 * n - 1)]
diag2 = [False for i in range(2 * n - 1)]
row = [False for i in range(n)]
print(rec(n, 0, 0))