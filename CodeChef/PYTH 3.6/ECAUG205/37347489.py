def is_valid(x):
    t = 0
    d = []

    for i in a:
        t += i // x

    return t >= k

def bins():
    l, r = 0, sum(a)

    while l < r:
        m = -(-(l + r) // 2)

        if is_valid(m):
            l = m
        else:
            r = m - 1

    return l

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    print(bins())