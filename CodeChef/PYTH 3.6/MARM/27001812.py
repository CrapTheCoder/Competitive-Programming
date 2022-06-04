for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if n % 2 and k > (n // 2):
        a[n // 2] = 0

    b = a.copy()

    for i in range(k % (n * 3)):
        b[i % n] = b[i % n] ^ b[n - (i % n) - 1]

    print(*b)
