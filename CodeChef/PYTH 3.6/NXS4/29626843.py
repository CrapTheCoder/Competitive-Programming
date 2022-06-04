for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    p = [0]

    for i in a:
        p.append(p[-1] + i)

    for _ in range(q):
        x, y = map(int, input().split())

        print(p[y] - p[x - 1])