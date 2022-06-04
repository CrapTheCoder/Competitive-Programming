for _ in range(int(input())):
    n, q = map(int, input().split())

    a = {}
    mp = {}

    c = 1
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1

        a[l] = a.get(l, []) + [c]
        a[r] = a.get(r, []) + [-c]
        c += 1

    spd = 0
    c = 0

    for i in range(n):
        r = 0
        if i in a:
            for j in a[i]:
                if j > 0:
                    mp[j] = i
                    c += 1

                if j < 0:
                    spd -= i - mp[-j] + 1
                    r += 1

        spd += c
        c -= r

        print(spd, end=' ')

    print()
