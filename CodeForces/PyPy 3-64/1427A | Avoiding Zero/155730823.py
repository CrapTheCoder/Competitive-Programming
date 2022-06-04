for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    if sum(a) == 0:
        print('NO')
 
    else:
        print('YES')
 
        pt = sum(i for i in a if i > 0)
        nt = -sum(i for i in a if i < 0)
 
        print(*sorted(a, reverse=pt>nt))