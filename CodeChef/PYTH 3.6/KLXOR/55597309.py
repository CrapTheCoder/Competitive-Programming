for _ in range(int(input())):
    n, k = map(int, input().split())
    s = ['~'] + list(map(int, input().strip()))

    p = [0]
    for i in range(1, n+1):
        p.append(p[-1] + s[i])

    t = 0
    for i in range(1, k+1):
        t += (p[i + (n-k)] - p[i-1]) & 1

    print(t)