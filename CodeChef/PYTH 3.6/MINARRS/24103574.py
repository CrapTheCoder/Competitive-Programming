for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = len(bin(max(a))) - 2

    b = []

    for i in a:
        r = bin(i)[2:]
        b.append('0' * (m - len(r)) + r)

    c = [0] * m

    for i in range(m):
        c[i] = sum(b[j][i] == '1' for j in range(n))

    x = ''

    for i in c:
        if n-i > i:
            x += '0'
        else:
            x += '1'

    x = int(x, 2)

    print(sum(i ^ x for i in a))
