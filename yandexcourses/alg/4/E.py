def rec(n, pos=0, s='', stack=''):
    if pos == n:
        print(s)
        return
    
    if n - pos <= len(stack) and len(stack) > 0:
        if stack[-1] == '(':
            rec(n, pos + 1, s + ')', stack[:-1])
        else:
            rec(n, pos + 1, s + ']', stack[:-1])

    else:
        rec(n, pos + 1, s + '(', stack + '(')
        rec(n, pos + 1, s + '[', stack + '[')

        if len(stack) > 0:
            if stack[-1] == '(':
                rec(n, pos + 1, s + ')', stack[:-1])
            else:
                rec(n, pos + 1, s + ']', stack[:-1])


n = int(input())
if n > 0 and n % 2 == 0:
    rec(n)