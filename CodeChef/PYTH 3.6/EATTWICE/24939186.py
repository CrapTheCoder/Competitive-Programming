for _ in range(int(input())):
    n, m = map(int, input().split())
    d = {}

    for i in range(n):
        di, vi = map(int, input().split())
        d[di] = max(d.get(di, 0), vi)

    ml = sorted(list(d.values()))
    print(ml[-1] + ml[-2])