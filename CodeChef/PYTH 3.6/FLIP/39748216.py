for _ in range(int(input())):
    a = list(input())
    b = list(input())
    n = len(a)

    t = 0

    for i in range(n):
        c = 0
        for j in range(i, n, 2):
            if a[j] == b[j]:
                break

            c += 1
            a[j] = b[j]

        if c:
            t += 1

    print(t)