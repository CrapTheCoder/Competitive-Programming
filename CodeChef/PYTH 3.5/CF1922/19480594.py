for _ in range(int(input())):
    n = int(input())

    b = list(map(int, input().split()))
    c = 0

    if 0 not in [b[0], b[1]] and b[0] > b[1] and b[0] % b[1] == 0:
        c += 1
    if 0 not in [b[0], b[1]] and b[-1] > b[-2] and b[-1] % b[-2] == 0:
        c += 1

    for i, j in enumerate(b[1:-1]):
        i += 1

        if 0 not in [b[i - 1], j, b[i + 1]] and b[i - 1] < j and b[i + 1] < j:
            if j % b[i - 1] == 0 and j % b[i + 1] == 0:
                c += 1

    print(c)