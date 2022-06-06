for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
 
    if sum(a) == m:
        print('YES')
    else:
        print('NO')