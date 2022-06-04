def solve(a, n, k):
    for i in range(n):
        if a[i] >= k:
            n = i
            break

    maxsum = 0
    x = y = 0

    for i in range(n):
        for j in range(i + 1, n):
            if k > a[i] + a[j] > maxsum:
                maxsum = a[i] + a[j]
                x, y = a[i], a[j]

    print(*sorted([x, y]))

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))

    solve(a, n, k)
