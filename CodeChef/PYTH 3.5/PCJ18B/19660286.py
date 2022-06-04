for _ in range(int(input())):
    n = int(input())
    dum = 0

    for i in range(1, n + 1, 2):
        dum += ((n - i) + 1) * ((n - i) + 1)

    print(dum)