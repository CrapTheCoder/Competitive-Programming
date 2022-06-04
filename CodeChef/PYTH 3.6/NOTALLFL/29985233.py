for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    d = {i: -1 for i in range(1, k + 1)}

    maxi = float('-inf')

    for i, j in enumerate(a):
        maxi = max(maxi, i - d[j] - 1)

        d[j] = i

    for i in range(1, k + 1):
        maxi = max(maxi, n - d[i] - 1)

    print(maxi)