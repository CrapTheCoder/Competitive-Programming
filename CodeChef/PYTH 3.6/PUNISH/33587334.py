for _ in range(int(input())):
    n, k = map(int, input().split())
    k -= 1

    if n == 1:
        print(1)
        continue

    x = k % (n*2 - 2) + 1

    if x <= n:
        print(x)
    else:
        print(n + (n - x))
