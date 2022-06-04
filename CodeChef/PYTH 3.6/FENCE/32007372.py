for _ in range(int(input())):
    n, m, k = map(int, input().split())

    s = set()

    for _ in range(k):
        r, c = map(int, input().split())

        s.add((r, c))

    ans = 0

    for i, j in s:
        if (i-1, j) not in s: ans += 1
        if (i+1, j) not in s: ans += 1
        if (i, j-1) not in s: ans += 1
        if (i, j+1) not in s: ans += 1

    print(ans)