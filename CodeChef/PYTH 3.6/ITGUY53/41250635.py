for _ in range(int(input())):
    n = int(input())

    for i in range(1, n+1):
        l = []

        for _ in range(i+1, n+i+1):
            l.append(_)

        print(*l, sep='')
