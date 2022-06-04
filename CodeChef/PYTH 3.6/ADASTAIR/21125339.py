for _ in range(int(input())):
    n, k = map(int, input().split())
    h = [0] + list(map(int, input().split()))

    s = 0

    for i in range(1, n + 1):
        x = h[i] - h[i - 1]

        s += (x // k) - (not x % k)

    print(s)

