c = [100, 50, 10, 5, 2, 1]

for _ in range(int(input())):
    n = int(input())
    i = 0

    s = 0

    while i < len(c):
        f = n // c[i]
        s += f

        n -= f * c[i]

        if n == 0:
            break

        i += 1

    print(s)