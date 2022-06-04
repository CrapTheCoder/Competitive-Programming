MOD = 10 ** 9 + 7

for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    s = set(a)

    mp = (float('inf'), float('inf'))

    for i in a:
        if (x ^ i) in s:
            a, b = i, x^i
            if a > b:
                a, b = b, a

            if mp[0] > a:
                mp = a, b

    if mp == (float('inf'), float('inf')):
        print(-1, -1)
    else:
        print(*mp)
