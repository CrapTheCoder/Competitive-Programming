for _ in range(int(input())):
    n = int(input())

    j = 2
    for i in range(1, n+1):
        l = []

        for _ in range(1, n+1):
            l.append(j)
            j += 2

        print(*l, sep='')
