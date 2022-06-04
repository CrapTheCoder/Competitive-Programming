for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))

    m = max(a)

    a.extend([m + 1] * k)

    print(a[(n + k) // 2])