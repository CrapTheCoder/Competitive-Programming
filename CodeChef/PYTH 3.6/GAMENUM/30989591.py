from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())

    mv = a ^ b
    mo = 0

    b = bin(b)[2:].zfill(len(bin(a)) - 2)

    o = 0

    copy = b

    while True:
        b = b[-1] + b[:-1]
        o += 1

        x = a ^ int(b, 2)

        if b == copy:
            break

        if x > mv:
            mv = x
            mo = o

    print(mo, mv)
