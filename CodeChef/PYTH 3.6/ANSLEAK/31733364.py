import random

choice = random.SystemRandom().choice

for _ in range(int(input())):
    n, m, k = map(int, input().split())

    d = []

    for i in range(n):
        a = list(map(int, input().split()))

        d.append(choice(a))

    print(*d)
