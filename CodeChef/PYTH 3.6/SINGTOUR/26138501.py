for _ in range(int(input())):
    n = int(input())
    lu = []

    for i in range(n):
        lu.append(list(map(int, input().split())) + [i, 0])

    lu = sorted(lu, reverse=True)
    for i in range(n): lu[i][3] += i

    lu.sort(key=lambda x: x[1])
    for i in range(n): lu[i][3] += i

    lu.sort(key=lambda x: x[2])
    print(*[i[3] for i in lu])
