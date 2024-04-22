def checksq(s):
  stack = ''
  op,cl = '([{ )]}'.split()
  for c in s:
    if c in op:
        stack += c
    elif c in cl:
        if stack == '':
            return False
        elif op[cl.index(c)] == stack[-1]:
            stack = stack[:-1]
        else:
           return False
    
  return stack == ''

a = input()
print(f'{"yes" if checksq(a) else "no"}')