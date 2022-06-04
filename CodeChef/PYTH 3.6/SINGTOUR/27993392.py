for _ in range(int(input())):
    n = int(input())

    lu = []
    d = [0] * n

    for i in range(n):
        lu.append((list(map(int, input().split())) + [i]))

    lu.sort(key=lambda x: x[0])

    for i in range(n):
        d[lu[i][2]] += n - i - 1

    lu.sort(key=lambda x: x[1])

    for i in range(n):
        d[lu[i][2]] += i

    lu.sort(key=lambda x: x[2])

    print(*d)