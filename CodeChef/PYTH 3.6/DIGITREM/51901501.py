for _ in range(int(input())):
    n, d = map(int, input().split())
    nn = n

    while str(d) in str(n):
        a = list(str(n))[::-1]
        i = 0

        while i < len(a):
            if int(a[i]) == d:
                if i == 0:
                    n += 1
                else:
                    x = ''.join(str(j) for j in a[:i])[::-1]
                    n += 10 ** len(x) - int(x)

                a = list(str(n))[::-1]

            i += 1

    print(n - nn)