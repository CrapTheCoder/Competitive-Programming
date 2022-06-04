for _ in range(int(input())):
    n, k, s = map(int, input().split())
    d = s // 7
    x = s
    m = 0
    a = 0
    i = s

    while s > 0:
        m += n
        s -= m // k
        m %= k
        a += 1

    if a + d > x:
        print(-1)
        continue
    print(a)