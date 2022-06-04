for _ in range(int(input())):
    n = int(input())

    l = list(map(int, input().split()))
    r = list(map(int, input().split()))

    mm = -1
    mi = -1
    mr = -1

    for i in range(n):
        a = l[i]
        b = r[i]
        c = a * b

        if c > mm:
            mm = c
            mi = i
            mr = b

        if c == mm and mr < b:
            mm = c
            mi = i
            mr = b

    print(mi + 1)
