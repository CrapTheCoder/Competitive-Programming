for _ in range(int(input())):
    n = int(input())
 
    if not (n & (n-1)):
        print('NO')
    else:
        print('YES')