input()

for n in map(int, input().split()):
    l = [1]
    for _ in range(n-1):
        l.append(l[-1] * 2 + 2)

    print(*l)

    l = [2]
    for _ in range(n-1):
        l.append(l[-1] * 2 + 1)

    print(*l)

    l = [4]
    for _ in range(n-1):
        l.append(l[-1] * 2 + 2)

    print(*l)

    l = [3]
    for _ in range(n-1):
        l.append(l[-1] * 2)

    print(*l)
