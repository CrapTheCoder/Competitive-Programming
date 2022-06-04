n, q = map(int, input().split())
b, e = 2 ** n, 2 ** (n + 1) - 2

c = 1
n += 1

for _ in range(q):
    l = input().split()

    if l[0] == '1':
        x = l[1]

        if x == '1' or x == '2':
            e = e * 2 + n
            b *= 2
            c *= 2

        if x == '3':
            e = e * 2 + c
            c = b
            n *= 2

        if x == '4':
            e = e * 2 + b
            b = c
            n *= 2

    else:
        print(e % 1000000007)
