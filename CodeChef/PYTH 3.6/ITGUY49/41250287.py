for _ in range(int(input())):
    n = int(input())

    j = 1
    for i in range(1, n+1):
        l = []

        for _ in range(1, n+1):
            l.append(j)
            j += 1

        print(*l, sep='')
