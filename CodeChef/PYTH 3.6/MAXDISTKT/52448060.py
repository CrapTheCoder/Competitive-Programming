for _ in range(int(input())):
    n = int(input())
    b = sorted(enumerate(map(int, input().split())), key=lambda x: x[1])

    x = []
    c = 0
    for i in range(n):
        c = min(c, b[i][1] - 1)
        x.append(c)
        c += 1

    a = [0] * n
    for i, j in enumerate(b):
        a[j[0]] = x[i]

    print(*a)