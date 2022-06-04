for _ in range(int(input())):
    n = int(input())
    s = ['*'] * n

    c = 0

    for i in range(n):
        l = []
        for j in range(i+1):
            c += 1
            l.append(c)

        if i % 2:
            l.reverse()

        print(*l, sep='*')