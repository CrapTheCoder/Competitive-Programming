for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    p = [0] * (n+1)

    for i in range(n):
        p[i+1] = a[i] ^ p[i]

    for _ in range(q):
        l, r = map(int, input().split())
        print((p[r] ^ p[l-1]) ^ (2 ** 31 - 1))
