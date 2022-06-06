for _ in range(int(input())):
    n = int(input())
    a = list(map(lambda x: int(x) % 2, input().split()))
 
    if sum(a) % 2:
        print('YES')
        continue
 
    if len(set(a)) == 1:
        if (a[0] * n) % 2:
            print('YES')
        else:
            print('NO')
 
        continue
 
    print('YES')