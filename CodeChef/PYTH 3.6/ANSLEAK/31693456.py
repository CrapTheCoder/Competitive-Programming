from random import shuffle

for _ in range(int(input())):
    n, m, k = map(int, input().split())

    d = []

    x = list(range(k))
    shuffle(x)

    for i in range(n):
        a = list(map(int, input().split()))

        d.append(a[x.pop()])

        if len(x) == 0:
            x = list(range(k))
            shuffle(x)

    print(*d)
