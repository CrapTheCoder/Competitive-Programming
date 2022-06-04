INF = float('-inf')

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(a[0], 1)
        print(0)
        continue

    dp = [[INF] * 2 for _ in range(n)]

    dp[0][0], dp[1][0], dp[1][1] = a[0], a[0] + a[1], a[0] * a[1]

    for i in range(2, n):
        dp[i][0], dp[i][1] = max(dp[i - 1]) + a[i], max(dp[i - 2]) + a[i - 1] * a[i]

    l = []

    i = n - 1

    while i > 0:
        if dp[i][0] <= dp[i][1]:
            l.append((i, i + 1))
            i -= 1

        i -= 1

    m = len(l)

    print(max(dp[-1]), n - m)
    print(m)

    for i, j in l[::-1]:
        print(i, j)
