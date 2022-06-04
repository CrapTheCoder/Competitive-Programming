for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    r = [0] * (n+1)

    for _ in range(int(input())):
        s, e, w = map(int, input().split())

        s -= 1
        e -= 1

        r[s] += w
        r[e+1] -= w

    for i in range(1, n+1):
        r[i] += r[i-1]

    print(sum(r) + sum(a))