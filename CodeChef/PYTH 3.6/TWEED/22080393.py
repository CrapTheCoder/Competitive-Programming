for _ in range(int(input())):
    n, p = input().split()
    a = list(map(int, input().split()))

    if int(n) == 1 and p == 'Dee' and a[0] % 2 == 0:
        print('Dee')
    else:
        print('Dum')