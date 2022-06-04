for _ in range(int(input())):
    n, u, d = map(int, input().split())
    h = list(map(int, input().split()))

    c = 1
    p = False

    for i in range(n-1):
        r = h[i+1] - h[i]

        if r > u:
            break
        if r < -d:
            if p: break
            else: p = True

        c += 1

    print(c)