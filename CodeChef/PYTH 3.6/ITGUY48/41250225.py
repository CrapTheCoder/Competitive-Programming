for _ in range(int(input())):
    n = int(input())

    for i in range(1, n+1):
        l = []

        for j in range(1, n+1):
            l.append(i*j)

        print(*l, sep='')