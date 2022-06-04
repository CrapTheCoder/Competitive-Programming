for _ in range(int(input())):
    n, x = map(int, input().split())

    if x % 2:
        if n % 2:
            print('Odd')
        else:
            print('Even')
    else:
        if n == 1:
            print('Even')
        else:
            print('Impossible')