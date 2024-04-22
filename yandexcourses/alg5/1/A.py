p, v = map(int, input().split())
q, m = map(int, input().split())

vm = [(p, v), (q, m)]
vm.sort()

if vm[0][0] == vm[1][0]:
    print(vm[1][1] * 2 + 1)
else:
    if vm[0][0] + vm[0][1] >= vm[1][0] - vm[1][1]:
        print(max(vm[0][0] + vm[0][1], vm[1][0] + vm[1][1]) 
              - min(vm[0][0] - vm[0][1], vm[1][0] - vm[1][1])
              + 1)
    else:
        print(2 * vm[0][1] + 2 * vm[1][1] + 2)
