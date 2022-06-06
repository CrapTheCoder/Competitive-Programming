for _ in range(int(input())):
    n = int(input())
    s = input()
 
    try:
        if n - s.index('8') < 11:
            print('NO')
        else:
            print('YES')
    except:
        print('NO')