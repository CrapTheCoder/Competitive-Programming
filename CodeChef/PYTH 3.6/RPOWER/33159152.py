def f(a, b, c, d, e):
    return (((a ^ b) | c) ^ d) | e

MAX = 2 ** 60 - 1

for _ in range(int(input())):
    a, b, d, e = map(int, input().split())

    c = list(bin(MAX)[2:][::-1])

    for i, j in enumerate(bin(a ^ b)[2:][::-1]):
        if c[i] == j == '1':
            c[i] = '0'

    for i, j in enumerate(bin(d)[2:][::-1]):
        if j == '1':
            c[i] = '0'

    for i, j in enumerate(bin(e)[2:][::-1]):
        if c[i] == j == '1':
            c[i] = '0'

    c = int(''.join(c)[::-1], 2)
    print(c)
