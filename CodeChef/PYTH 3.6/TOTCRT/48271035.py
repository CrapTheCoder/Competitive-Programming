for _ in range(int(input())):
    n = int(input())
    d = {}

    for _ in range(3):
        for _ in range(n):
            s, c = input().split()
            d[s] = d.get(s, 0) + int(c)

    print(*sorted(d.values()))