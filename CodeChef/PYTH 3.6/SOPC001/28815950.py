for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))

    c = 1
    s = 0

    for i in range(n):
        if a[i] == a[-1]:
            break

        c += 1
        s += a[-1] - a[i]

    print(s, c)