for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    d = {}
    count = 0

    for i in a:
        d[i] = 1
    for i in b:
        d[i] = d.get(i, 0) + 1
    for i in d:
        if d[i] == 2: count += 1

    print(count, n - len(d))