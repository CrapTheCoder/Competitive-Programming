n, q = map(int, input().split())

top = 1
bottom = 2 ** n
depth = n + 1
edges = 2 ** (n + 1) - 2

for _ in range(q):
    x = list(map(int, input().split()))

    if x[0] == 2:
        print(edges % (10 ** 9 + 7))
    else:
        t = x[1]

        edges *= 2

        if t == 1 or t == 2:
            top *= 2
            bottom *= 2

            edges += depth

        if t == 3:
            depth *= 2
            edges += top
            top = bottom

        if t == 4:
            depth *= 2
            edges += bottom
            bottom = top
