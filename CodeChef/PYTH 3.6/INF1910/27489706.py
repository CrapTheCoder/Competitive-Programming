for _ in range(int(input())):
    n, q = map(int, input().split())
    l = list(range(1, n+1))

    m = []

    s = 0

    while l:
        s = (s + 1) % n
        m.append(l.pop(s))

        n -= 1

    for __ in range(q):
        print(m[int(input()) - 1])
