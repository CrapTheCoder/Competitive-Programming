for _ in range(int(input())):
    n, k = map(int, input().split())

    a = list(range(1, n + 1))

    if n == k:
        print(*a)
        continue

    a = a[:k] + [a[-1]] + a[k:-1]

    c = 0
    for i in range(n):
        if a[i] == i+1:
            c += 1

    if c != k:
        print(-1)
    else:
        print(*a)