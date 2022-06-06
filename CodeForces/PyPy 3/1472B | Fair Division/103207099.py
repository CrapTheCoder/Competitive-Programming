for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    c1 = a.count(1)
    c2 = n - c1
 
    a = b = 0
 
    if c2 % 2 == 0:
        if c1 % 2 == 0:
            print('YES')
        else:
            print('NO')
 
    else:
        if c1 >= 2 and c1 % 2 == 0:
            print('YES')
        else:
            print('NO')