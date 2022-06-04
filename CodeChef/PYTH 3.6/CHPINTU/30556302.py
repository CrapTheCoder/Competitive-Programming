for _ in range(int(input())):
    n, t = map(int, input().split())
    f = list(map(int, input().split()))
    p = list(map(int, input().split()))

    d = {}

    for i, j in zip(f, p):
        d[i] = d.get(i, 0) + j

    print(min(d.values()))