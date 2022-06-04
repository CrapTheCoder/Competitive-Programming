for _ in range(int(input())):
    n, d = map(int, input().split())
    a = sorted(map(int, input().split()))
 
    for i in a:
        if i > d:
            break
 
    else:
        print('YES')
        continue
 
    if a[0] + a[1] > d:
        print('NO')
        continue
 
    print('YES')