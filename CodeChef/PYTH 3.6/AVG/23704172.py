for _ in range(int(input())):
    n, k, v = map(int, input().split())
    a = list(map(int, input().split()))

    x = (v * (n + k) - sum(a)) / k

    if int(x) == float(x) and int(x) > 0: print(int(x))
    else: print(-1)
