from sys import stdin
input = stdin.readline

MAX = 60

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        done = set()

        for j in range(MAX):
            asd = (1 << j)

            if asd >= a[i]:
                break

            x = a[i] % asd
            if (x != 0) and (x not in done):
                a.append(x)
                done.add(x)

    p = [0] * MAX

    for i in a:
        p[i.bit_length() - 1] += 1

    for i in range(1, MAX):
        p[i] += p[i-1] >> 1

    s = 0
    for i in range(MAX):
        if p[i]:
            s += 1 << i

    print(s)
