for _ in range(int(input())):
    n = int(input())
 
    r = n // 2020
    x = r * 2020
 
    if n - x <= r:
        print('YES')
    else:
        print('NO')