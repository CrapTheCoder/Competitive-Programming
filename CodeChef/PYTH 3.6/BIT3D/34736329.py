from sys import setrecursionlimit
setrecursionlimit(10 * 9)

def solve(i):
    if i + k >= n:
        return 1

    if i in dp:
        return dp[i]

    mini = float('inf')
    for j in range(i+1, min(n, i+k+1)):
        if i == -1 or a[i] == a[j]:
            mini = min(mini, solve(j) + 1)

    dp[i] = mini
    return dp[i]


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(lambda x: int(x) % 2, input().split()))

    le = lo = -1
    se = so = -1

    for i in range(n-k, n):
        if a[i] == 0:
            le = i
            break

    for i in range(n-k, n):
        if a[i] == 1:
            lo = i
            break

    m1 = float('inf')
    if le != -1:
        m1 = 0
        while True:
            lle = -1

            for i in range(se + 1, se + k + 1):
                if i == le:
                    m1 += 2
                    break

                if a[i] == 0:
                    lle = i

            else:
                if lle == -1:
                    m1 = float('inf')
                    break

                se = lle
                m1 += 1
                continue

            break

    m2 = float('inf')
    if lo != -1:
        m2 = 0
        while True:
            llo = -1

            for i in range(so + 1, so + k + 1):
                if i == lo:
                    m2 += 2
                    break

                if a[i] == 1:
                    llo = i

            else:
                if llo == -1:
                    m2 = float('inf')
                    break

                so = llo
                m2 += 1
                continue

            break

    if min(m1, m2) != float('inf'):
        print(min(m1, m2))
    else:
        print(-1)