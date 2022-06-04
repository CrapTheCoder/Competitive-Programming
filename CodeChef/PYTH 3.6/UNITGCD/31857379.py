for _ in range(int(input())):
    n = int(input())

    print(max(1, n // 2))

    print(min(n, 3), *range(1, min(n, 3) + 1))

    if n <= 3:
        continue

    for i in range(4, n+1, 2):
        if i + 1 <= n:
            print(2, i, i+1)
        else:
            print(1, n)
