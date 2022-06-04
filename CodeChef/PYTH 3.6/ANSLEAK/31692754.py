from random import choice

for _ in range(int(input())):
    n, m, k = map(int, input().split())

    d = []

    for i in range(n):
        a = list(map(int, input().split()))

        d.append(a[i])

    print(*d)
