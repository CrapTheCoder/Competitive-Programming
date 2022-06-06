for _ in range(int(input())):
    a, b, n, s = map(int, input().split())
 
    if a * n + b >= s:
        if n * (s // n) + b >= s:
            print('yes')
        else:
            print('no')
    else:
        print('no')