from random import randint

for _ in range(int(input())):
    n, m, k = map(int, input().split())

    start = randint(0, k-1)

    d = []

    for _ in range(n):
        a = list(map(int, input().split()))

        d.append(a[start])

        start = (start - 1) % k

    print(*d)
